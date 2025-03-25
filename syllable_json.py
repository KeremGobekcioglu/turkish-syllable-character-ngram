
import json
from collections import defaultdict
import heapq
from tqdm import tqdm  # Progress bar

# Function to generate N-Grams
def generate_ngrams(tokens, n):
    ngrams = defaultdict(int)  # Dictionary to store N-Grams and their counts
    # Use tqdm to show progress on token processing
    for i in tqdm(range(len(tokens) - n + 1), desc=f"Generating {n}-Grams"):
        ngram = tuple(tokens[i:i + n])  # Get the N-Gram as a tuple
        ngrams[ngram] += 1  # Increment the count for this N-Gram
    print(f"{n}-grams generated")
    return ngrams

# Function to get the top N N-Grams without sorting the entire set
def get_top_n_ngrams(ngrams, top_n=20):
    # Use heapq.nlargest to find the top N most frequent N-Grams
    top_ngrams = heapq.nlargest(top_n, ngrams.items(), key=lambda x: x[1])
    return top_ngrams

# Convert the N-Gram dictionary into a list of lists for JSON serialization
def convert_ngrams_to_list(ngrams):
    # Ensure that ngrams is a list of tuples before trying to unpack
    if isinstance(ngrams, dict):
        return [[list(key), value] for key, value in ngrams.items()]
    elif isinstance(ngrams, list):
        return [[list(key), value] for key, value in ngrams if isinstance(key, tuple) and isinstance(value, int)]
    else:
        raise ValueError("Expected a dictionary or a list of tuples")

# Function to process the syllable-based model from a file
def process_syllable_based(file_path, top_n=20):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().strip

    syllables = text.split()

    unigrams = generate_ngrams(syllables, 1)
    bigrams = generate_ngrams(syllables, 2)
    trigrams = generate_ngrams(syllables, 3)

    # Get the top 20 unigrams for comparing the counts
    top_20_unigrams = get_top_n_ngrams(unigrams, 20)
    top_20_bigrams = get_top_n_ngrams(bigrams, 20)
    top_20_trigrams = get_top_n_ngrams(trigrams, 20)

    return top_20_unigrams, top_20_bigrams, top_20_trigrams, unigrams, bigrams, trigrams

# Example usage
syllable_file = "syllable_based_model_test.txt"  # Replace with your syllable-based text file

# Syllable-based N-Gram generation from a file

top_20_unigrams, top_20_bigrams, top_20_trigrams, syllable_unigrams, syllable_bigrams, syllable_trigrams = process_syllable_based(syllable_file)
output_prefix = "syllable_test_data"  # Prefix for the output files
with open(f"{output_prefix}_.json", 'w', encoding='utf-8') as output_file:
    json.dump({
        "top_20_unigrams": convert_ngrams_to_list(top_20_unigrams),
        "unigrams": convert_ngrams_to_list(syllable_unigrams),
    }, output_file, ensure_ascii=False, indent=4)

with open(f"{output_prefix}_bigrams.json", 'w', encoding='utf-8') as output_file:
    json.dump({
        "top_20_bigrams": convert_ngrams_to_list(top_20_bigrams),
        "bigrams": convert_ngrams_to_list(syllable_bigrams)
    }, output_file, ensure_ascii=False, indent=4)

with open(f"{output_prefix}_trigrams.json", 'w', encoding='utf-8') as output_file:
    json.dump({
        "top_20_trigrams": convert_ngrams_to_list(top_20_trigrams),
        "trigrams": convert_ngrams_to_list(syllable_trigrams)
    }, output_file, ensure_ascii=False, indent=4)
    


print("N-Gram generation completed and saved to separate files.")