import json
from collections import defaultdict
from tqdm import tqdm  # Import tqdm for progress bar

# Function to generate N-Grams
def generate_ngrams(tokens, n):
    ngrams = defaultdict(int)  # Dictionary to store N-Grams and their counts
    # Use tqdm to display progress as N-Grams are being generated
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

# Function to process the syllable-based model from a file
def process_syllable_based(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().strip()  # Read the file content

    # Split the text into syllables using spaces (since syllables are already space-separated)
    syllables = text.split()  # This ensures that we're counting syllables, not characters
    print("syllables generated")

    # Generate N-Grams with tqdm progress bars
    unigrams = generate_ngrams(syllables, 1)
    bigrams = generate_ngrams(syllables, 2)
    trigrams = generate_ngrams(syllables, 3)

    return unigrams, bigrams, trigrams

# Example Usage
syllable_file = "test_s.txt"  # Replace with your syllable-based text file
print("file name = " + syllable_file)

# Syllable-based N-Gram generation from a file
syllable_unigrams, syllable_bigrams, syllable_trigrams = process_syllable_based(syllable_file)

# Get the top 10 N-Grams for syllable-based model
top_10_syllable_unigrams = get_top_n_ngrams(syllable_unigrams, 20)
top_10_syllable_bigrams = get_top_n_ngrams(syllable_bigrams, 20)
top_10_syllable_trigrams = get_top_n_ngrams(syllable_trigrams, 20)

# Count N-Grams that appear at least 5 times
syllable_unigrams_min_5 = count_ngrams_with_min_count(syllable_unigrams, 5)
syllable_bigrams_min_5 = count_ngrams_with_min_count(syllable_bigrams, 5)
syllable_trigrams_min_5 = count_ngrams_with_min_count(syllable_trigrams, 5)

# Count unique N-Grams (appear only once)
syllable_unigrams_unique = count_unique_ngrams(syllable_unigrams)
syllable_bigrams_unique = count_unique_ngrams(syllable_bigrams)
syllable_trigrams_unique = count_unique_ngrams(syllable_trigrams)

# Print results for syllable-based model
print("Syllable-based Unigrams - Top 10:", top_10_syllable_unigrams)
print("Syllable-based Bigrams - Top 10:", top_10_syllable_bigrams)
print("Syllable-based Trigrams - Top 10:", top_10_syllable_trigrams)
print("Syllable-based Unigrams - Count of Unique:", syllable_unigrams_unique)
print("Syllable-based Bigrams - Count of Unique:", syllable_bigrams_unique)
print("Syllable-based Trigrams - Count of Unique:", syllable_trigrams_unique)
print("Syllable-based Unigrams - Count Appearing At Least 5 Times:", syllable_unigrams_min_5)
print("Syllable-based Bigrams - Count Appearing At Least 5 Times:", syllable_bigrams_min_5)
print("Syllable-based Trigrams - Count Appearing At Least 5 Times:", syllable_trigrams_min_5)
