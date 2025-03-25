import random
import json
from collections import defaultdict
import math
# Function for Good-Turing Smoothing
def good_turing_smoothing(ngrams):
    # Frequency of Frequencies
    frequency_of_frequencies = defaultdict(int)
    for count in ngrams.values():
        frequency_of_frequencies[count] += 1

    # Applying Good-Turing adjustment
    adjusted_counts = {}
    total_tokens = sum(ngrams.values())

    for ngram, count in ngrams.items():
        if count + 1 in frequency_of_frequencies:
            # Applying Good-Turing adjustment for observed N-Grams
            adjusted_count = (count + 1) * (frequency_of_frequencies[count + 1] / frequency_of_frequencies[count])
        else:
            # If no N_{r+1}, use the original count
            adjusted_count = count
        adjusted_counts[ngram] = adjusted_count

    probabilities = {}
    for ngram, adjusted_count in adjusted_counts.items():
        probabilities[ngram] = adjusted_count / total_tokens

    # Probability for unseen N-Grams
    unseen_probability = frequency_of_frequencies[1] / total_tokens if 1 in frequency_of_frequencies else 0

    return probabilities, unseen_probability

def generate_random_sentence_with_smoothing(ngram_probabilities, unseen_probability, n, sentence_length=10):
    sentence = []
    # Start with a random N-Gram from the model
    current_ngram = random.choice(list(ngram_probabilities.keys()))
    sentence.extend(current_ngram)
    
    while len(sentence) < sentence_length:
        # Filter to get only N-Grams that continue from the last part of the sentence
        candidates = [(ngram, prob) for ngram, prob in ngram_probabilities.items() if ngram[:n-1] == tuple(sentence[-(n-1):])]
        
        # Use the top 5 candidates based on their probabilities
        if candidates:
            top_candidates = sorted(candidates, key=lambda x: x[1], reverse=True)[:5]
            next_ngram = random.choices(
                [ngram for ngram, _ in top_candidates],
                weights=[prob for _, prob in top_candidates]
            )[0]
        else:
            # If no matching N-Gram is found, pick a random N-Gram with the unseen probability as fallback
            next_ngram = random.choices(
                list(ngram_probabilities.keys()),
                weights=[unseen_probability] * len(ngram_probabilities)
            )[0]
        
        # Append only the new part of the N-Gram
        sentence.append(next_ngram[-1])
    return " ".join(sentence)

# Function to precompute the top 5 N-Grams for quick access
def get_top_5_ngrams(ngram_probabilities):
    top_5_ngrams = {}
    for ngram, prob in ngram_probabilities.items():
        prefix = ngram[:-1]  # Use n-1 elements as the prefix for each n-gram
        if prefix not in top_5_ngrams:
            top_5_ngrams[prefix] = []
        top_5_ngrams[prefix].append((ngram, prob))
        # Keep only the top 5 sorted by probability
        top_5_ngrams[prefix] = sorted(top_5_ngrams[prefix], key=lambda x: x[1], reverse=True)[:5]
    return top_5_ngrams

# Generate random sentence based on the top 5 N-Grams
def generate_random_sentence_with_top_5(ngram_probabilities, unseen_probability, n, sentence_length=10):
    top_5_ngrams = get_top_5_ngrams(ngram_probabilities)
    sentence = []
    
    # Start with a random N-Gram from the model
    current_ngram = random.choice(list(ngram_probabilities.keys()))
    sentence.extend(current_ngram)
    
    while len(sentence) < sentence_length:
        # Get top 5 choices based on current context
        context = tuple(sentence[-(n-1):])  # Last n-1 words of the sentence
        candidates = top_5_ngrams.get(context, [])

        if candidates:
            # Randomly select one of the top 5 N-Grams
            next_ngram = random.choices(
                [ngram for ngram, _ in candidates],
                weights=[prob for _, prob in candidates]
            )[0]
        else:
            # If no matching N-Gram is found, try another random context from top_5_ngrams
            # print("No candidates found, selecting a new context from top_5_ngrams.")
            new_context = random.choice(list(top_5_ngrams.keys()))
            next_ngram = random.choice(top_5_ngrams[new_context])[0]
        # Append only the new part of the N-Gram
        sentence.append(next_ngram[-1])
    
    return " ".join(sentence)


def generate_random_sentence_hybrid(ngram_probabilities, unseen_probability, n, sentence_length=10):
    top_5_ngrams = get_top_5_ngrams(ngram_probabilities)
    sentence = []
    
    # Start with a random N-Gram from the model
    current_ngram = random.choice(list(ngram_probabilities.keys()))
    sentence.extend(current_ngram)
    
    while len(sentence) < sentence_length:
        context = tuple(sentence[-(n-1):])
        candidates = top_5_ngrams.get(context, [])
        
        if candidates:
            # Include unseen probability to allow some randomness within top 5 candidates
            candidate_ngrams = [ngram for ngram, _ in candidates] + [None]
            weights = [prob for _, prob in candidates] + [unseen_probability]
            next_ngram = random.choices(candidate_ngrams, weights=weights)[0]
            
            if next_ngram is None:
                # print("icerdeyim\n")
                # If unseen probability is chosen, pick a random n-gram
                next_ngram = random.choice(list(ngram_probabilities.keys()))
        else:
            # If no candidates found, use unseen probability for a random choice
            next_ngram = random.choice(list(ngram_probabilities.keys()))
        
        sentence.append(next_ngram[-1])

    return " ".join(sentence)
def load_test_data(file_path , flag):
    print("loading test data")
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().strip()
    # Tokenize the text; adjust as needed (e.g., split by spaces for syllables or words)
    tokens = text.split() if flag else list(text)
    return tokens

def calculate_perplexity(test_data, ngram_probabilities, unseen_probability, n):
    log_prob_sum = 0
    N = len(test_data)
    print("calculating perplexity")
    for i in range(N - n + 1):
        # Get the current n-gram from the test data
        current_ngram = tuple(test_data[i:i + n])
        
        # Get the probability from the model or use the unseen probability
        probability = ngram_probabilities.get(current_ngram, unseen_probability)
        
        # Add the log probability to the sum
        if probability > 0:
            log_prob_sum += math.log2(probability)
        else:
            log_prob_sum += math.log2(unseen_probability)
    
    # Calculating perplexity
    perplexity = 2 ** (-log_prob_sum / (N - n + 1))
    return perplexity

# Load the JSON file containing N-Grams and their counts
with open("syllable_train_unigrams.json", "r", encoding="utf-8") as f:
    data = json.load(f)
with open("syllable_train_bigrams.json", "r", encoding="utf-8") as f:
    data2 = json.load(f)
with open("syllable_train_trigrams.json", "r", encoding="utf-8") as f:
    data3 = json.load(f)
with open("character_n_grams_train.json", "r", encoding="utf-8") as f:
    data4 = json.load(f)
# Extract N-Grams as dictionaries
unigram_counts = {tuple(item[0]): item[1] for item in data["unigrams"]}
bigram_counts = {tuple(item[0]): item[1] for item in data2["bigrams"]}
trigram_counts = {tuple(item[0]): item[1] for item in data3["trigrams"]}
char_unigrams = {tuple(item[0]): item[1] for item in data4["unigrams"]}
char_bigrams = {tuple(item[0]): item[1] for item in data4["bigrams"]}
char_trigrams = {tuple(item[0]): item[1] for item in data4["trigrams"]}

unigram_probabilities, unigram_unseen_prob = good_turing_smoothing(unigram_counts)
bigram_probabilities, bigram_unseen_prob = good_turing_smoothing(bigram_counts)
trigram_probabilities, trigram_unseen_prob = good_turing_smoothing(trigram_counts)
char_unigram_probabilities, char_unigram_unseen_prob = good_turing_smoothing(char_unigrams)
char_bigram_probabilities, char_bigram_unseen_prob = good_turing_smoothing(char_bigrams)
char_trigram_probabilities, char_trigram_unseen_prob = good_turing_smoothing(char_trigrams)

test_tokens = load_test_data('character_based_model_test.txt' , False)  # Adjust to your test file path

# Generate test data for unigrams, bigrams, and trigrams
char_test_unigrams = test_tokens  # Each token is a unigram
char_test_bigrams = [tuple(test_tokens[i:i+2]) for i in range(len(test_tokens) - 1)]
char_test_trigrams = [tuple(test_tokens[i:i+3]) for i in range(len(test_tokens) - 2)]

# test_tokens = load_test_data('syllable_based_model_test.txt' , True)  # Adjust to your test file path

# Generate test data for unigrams, bigrams, and trigrams
syllable_test_unigrams = test_tokens  # Each token is a unigram
syllable_test_bigrams = [tuple(test_tokens[i:i+2]) for i in range(len(test_tokens) - 1)]
syllable_test_trigrams = [tuple(test_tokens[i:i+3]) for i in range(len(test_tokens) - 2)]

char_unigram_perplexity = calculate_perplexity(char_test_unigrams, char_unigram_probabilities, char_unigram_unseen_prob, 1)
char_bigram_perplexity = calculate_perplexity(char_test_bigrams, char_bigram_probabilities, char_bigram_unseen_prob, 2)
char_trigram_perplexity = calculate_perplexity(char_test_trigrams, char_trigram_probabilities, char_trigram_unseen_prob, 3)

syllable_unigram_perplexity = calculate_perplexity(syllable_test_unigrams, unigram_probabilities, unigram_unseen_prob, 1)
syllable_bigram_perplexity = calculate_perplexity(syllable_test_bigrams, bigram_probabilities, bigram_unseen_prob, 2)
syllable_trigram_perplexity = calculate_perplexity(syllable_test_trigrams, trigram_probabilities, trigram_unseen_prob, 3)

print(f"Character Unigram Perplexity: {char_unigram_perplexity}")
print(f"Character Bigram Perplexity: {char_bigram_perplexity}")
print(f"Character Trigram Perplexity: {char_trigram_perplexity}")

print(f"Syllable Unigram Perplexity: {syllable_unigram_perplexity}")
print(f"Syllable Bigram Perplexity: {syllable_bigram_perplexity}")
print(f"Syllable Trigram Perplexity: {syllable_trigram_perplexity}")


print(f"Unseen char unigram Probability: {char_unigram_unseen_prob}")
print(f"Unseen char bigram Probability: {char_bigram_unseen_prob}")
print(f"Unseen char trigram Probability: {char_trigram_unseen_prob}")
print("Character Based Model Sentences")
sentence = generate_random_sentence_with_smoothing(char_unigram_probabilities, char_unigram_unseen_prob, 1, 20)
print("smooth uni ->" + sentence)
sentence = generate_random_sentence_with_top_5(char_unigram_probabilities, char_unigram_unseen_prob, 1, 20)
print("top5_uni ->" + sentence)
sentence = generate_random_sentence_hybrid(char_unigram_probabilities, char_unigram_unseen_prob, 1, 20)
print("hybrid_uni ->" + sentence)
sentence = generate_random_sentence_with_smoothing(char_unigram_probabilities, char_unigram_unseen_prob, 1, 20)
print("smooth uni ->" + sentence)
sentence = generate_random_sentence_with_top_5(char_unigram_probabilities, char_unigram_unseen_prob, 1, 20)
print("top5_uni ->" + sentence)
sentence = generate_random_sentence_hybrid(char_unigram_probabilities, char_unigram_unseen_prob, 1, 20)
print("hybrid_uni ->" + sentence)
sentence = generate_random_sentence_with_smoothing(char_bigram_probabilities, char_bigram_unseen_prob, 2, 20)
print("smooth_bi->" + sentence)
sentence = generate_random_sentence_with_top_5(char_bigram_probabilities, char_bigram_unseen_prob, 2, 20)
print("top_5_bigram ->" + sentence)
sentence = generate_random_sentence_hybrid(char_bigram_probabilities, char_bigram_unseen_prob, 2, 20)
print("hybrid_bigram ->" + sentence)
sentence = generate_random_sentence_with_smoothing(char_bigram_probabilities, char_bigram_unseen_prob, 2, 20)
print("smooth_bi->" + sentence)
sentence = generate_random_sentence_with_top_5(char_bigram_probabilities, char_bigram_unseen_prob, 2, 20)
print("top_5_bigram ->" + sentence)
sentence = generate_random_sentence_hybrid(char_bigram_probabilities, char_bigram_unseen_prob, 2, 20)
print("hybrid_bigram ->" + sentence)
sentence = generate_random_sentence_with_smoothing(char_trigram_probabilities, char_trigram_unseen_prob, 3, 20)
print("smooth_tri ->"  + sentence)
sentence = generate_random_sentence_with_top_5(char_trigram_probabilities, char_trigram_unseen_prob, 3, 20)
print("top5_tri ->" + sentence)
sentence = generate_random_sentence_hybrid(char_trigram_probabilities, char_trigram_unseen_prob, 3, 20)
print("hybrid_tri->" + sentence)
sentence = generate_random_sentence_with_smoothing(char_trigram_probabilities, char_trigram_unseen_prob, 3, 20)
print("smooth_tri ->"  + sentence)
sentence = generate_random_sentence_with_top_5(char_trigram_probabilities, char_trigram_unseen_prob, 3, 20)
print("top5_tri ->" + sentence)
sentence = generate_random_sentence_hybrid(char_trigram_probabilities, char_trigram_unseen_prob, 3, 20)
print("hybrid_tri->" + sentence)


print(f"Unseen unigram Probability: {unigram_unseen_prob}")
print(f"Unseen bigram Probability: {bigram_unseen_prob}")
print(f"Unseen trigram Probability: {trigram_unseen_prob}")
print("Syllable Based Model Sentences")
sentence = generate_random_sentence_with_smoothing(unigram_probabilities, unigram_unseen_prob, 1, 20)
print("smooth uni ->" + sentence)
sentence = generate_random_sentence_with_top_5(unigram_probabilities, unigram_unseen_prob, 1, 20)
print("top5_uni ->" + sentence)
sentence = generate_random_sentence_hybrid(unigram_probabilities, unigram_unseen_prob, 1, 20)
print("hybrid_uni ->" + sentence)
sentence = generate_random_sentence_with_smoothing(unigram_probabilities, unigram_unseen_prob, 1, 20)
print("smooth uni ->" + sentence)
sentence = generate_random_sentence_with_top_5(unigram_probabilities, unigram_unseen_prob, 1, 20)
print("top5_uni ->" + sentence)
sentence = generate_random_sentence_hybrid(unigram_probabilities, unigram_unseen_prob, 1, 20)
print("hybrid_uni ->" + sentence)
sentence = generate_random_sentence_with_smoothing(bigram_probabilities, bigram_unseen_prob, 2, 20)
print("smooth_bi->" + sentence)
sentence = generate_random_sentence_with_top_5(bigram_probabilities, bigram_unseen_prob, 2, 20)
print("top_5_bigram ->" + sentence)
sentence = generate_random_sentence_hybrid(bigram_probabilities, bigram_unseen_prob, 2, 20)
print("hybrid_bigram ->" + sentence)
sentence = generate_random_sentence_with_smoothing(bigram_probabilities, bigram_unseen_prob, 2, 20)
print("smooth_bi->" + sentence)
sentence = generate_random_sentence_with_top_5(bigram_probabilities, bigram_unseen_prob, 2, 20)
print("top_5_bigram ->" + sentence)
sentence = generate_random_sentence_hybrid(bigram_probabilities, bigram_unseen_prob, 2, 20)
print("hybrid_bigram ->" + sentence)
sentence = generate_random_sentence_with_smoothing(trigram_probabilities, trigram_unseen_prob, 3, 20)
print("smooth_tri ->"  + sentence)
sentence = generate_random_sentence_with_top_5(trigram_probabilities, trigram_unseen_prob, 3, 20)
print("top5_tri ->" + sentence)
sentence = generate_random_sentence_hybrid(trigram_probabilities, trigram_unseen_prob, 3, 20)
print("hybrid_tri->" + sentence)
sentence = generate_random_sentence_with_smoothing(trigram_probabilities, trigram_unseen_prob, 3, 20)
print("smooth_tri ->"  + sentence)
sentence = generate_random_sentence_with_top_5(trigram_probabilities, trigram_unseen_prob, 3, 20)
print("top5_tri ->" + sentence)
sentence = generate_random_sentence_hybrid(trigram_probabilities, trigram_unseen_prob, 3, 20)
print("hybrid_tri->" + sentence)