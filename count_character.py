import json
from collections import defaultdict
from tqdm import tqdm  # Progress bar

def generate_ngrams(tokens, n):
    ngrams = defaultdict(int)  # Dictionary to store N-Grams and their counts
    # Use tqdm to show progress on token processing
    for i in tqdm(range(len(tokens) - n + 1), desc=f"Generating {n}-Grams"):
        ngram = tuple(tokens[i:i + n])  # Get the N-Gram as a tuple
        ngrams[ngram] += 1  # Increment the count for this N-Gram
    print(f"{n}-grams generated")
    return ngrams


# Function to get the top N most frequent N-Grams
def get_top_n_ngrams(ngrams, top_n=10):
    return sorted(ngrams.items(), key=lambda x: x[1], reverse=True)[:top_n]

# Function to count N-Grams that appear at least min_count times
def count_ngrams_with_min_count(ngrams, min_count=5):
    return sum(1 for count in ngrams.values() if count >= min_count)

# Function to count unique N-Grams (appear only once)
def count_unique_ngrams(ngrams):
    return sum(1 for count in ngrams.values() if count == 1)

# Convert the N-Gram dictionary into a list of lists for JSON serialization
def convert_ngrams_to_list(ngrams):
    return [[list(key), value] for key, value in ngrams.items()]

def process_character_based(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().strip()
    characters = text  # Characters are not splitted because they had been already splitted
    print("characters generated")
    # Generate N-Grams
    unigrams = generate_ngrams(characters, 1)
    bigrams = generate_ngrams(characters, 2)
    trigrams = generate_ngrams(characters, 3)

    return unigrams, bigrams, trigrams
# Example Usage
character_file = "character_based_model_test.txt"  # Replace with your character-based text file

# Character-based N-Gram generation from a file
char_unigrams, char_bigrams, char_trigrams = process_character_based(character_file)

# Get the top 10 N-Grams for character-based model
top_10_char_unigrams = get_top_n_ngrams(char_unigrams, 10)
top_10_char_bigrams = get_top_n_ngrams(char_bigrams, 10)
top_10_char_trigrams = get_top_n_ngrams(char_trigrams, 10)

# Count N-Grams that appear at least 5 times
char_unigrams_min_5 = count_ngrams_with_min_count(char_unigrams, 5)
char_bigrams_min_5 = count_ngrams_with_min_count(char_bigrams, 5)
char_trigrams_min_5 = count_ngrams_with_min_count(char_trigrams, 5)

# Count unique N-Grams (appear only once)
char_unigrams_unique = count_unique_ngrams(char_unigrams)
char_bigrams_unique = count_unique_ngrams(char_bigrams)
char_trigrams_unique = count_unique_ngrams(char_trigrams)

# Print results for character-based model
print("Character-based Unigrams - Top 10:", top_10_char_unigrams)
print("Character-based Bigrams - Top 10:", top_10_char_bigrams)
print("Character-based Trigrams - Top 10:", top_10_char_trigrams)
print("Character-based Unigrams - Count of Unique:", char_unigrams_unique)
print("Character-based Bigrams - Count of Unique:", char_bigrams_unique)
print("Character-based Trigrams - Count of Unique:", char_trigrams_unique)
print("Character-based Unigrams - Count Appearing At Least 5 Times:", char_unigrams_min_5)
print("Character-based Bigrams - Count Appearing At Least 5 Times:", char_bigrams_min_5)
print("Character-based Trigrams - Count Appearing At Least 5 Times:", char_trigrams_min_5)