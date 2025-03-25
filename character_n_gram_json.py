import json
from collections import defaultdict
from tqdm import tqdm  # Progress bar
import heapq
# Function to generate N-Grams
def generate_ngrams(tokens, n):
    ngrams = defaultdict(int)  # Default dic to store N-Grams and their counts
    # Use tqdm to show progress on token processing
    for i in tqdm(range(len(tokens) - n + 1), desc=f"Generating {n}-Grams"):
        ngram = tuple(tokens[i:i + n])  # Get the N-Gram as a tuple
        ngrams[ngram] += 1  # Increment the count for this N-Gram
    print(f"{n}-grams generated")
    return ngrams

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

# Function to process the character-based model from a file
def process_character_based(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().strip()
    print("text read")
    characters = text # Characters are not splitted because they had been already splitted
    unigrams = generate_ngrams(characters, 1)
    print("character uni")
    bigrams = generate_ngrams(characters, 2)
    print("character bi")
    trigrams = generate_ngrams(characters, 3)
    print("character tri")
    
    top_20_unigrams = get_top_n_ngrams(unigrams, 20)
    top_20_bigrams = get_top_n_ngrams(bigrams, 20)
    top_20_trigrams = get_top_n_ngrams(trigrams, 20)
    
    return  top_20_unigrams,top_20_bigrams,top_20_trigrams,unigrams, bigrams, trigrams

character_file = "character_based_model_test.txt"

top_20_unigrams,top_20_bigrams,top_20_trigrams,char_unigrams, char_bigrams, char_trigrams = process_character_based(character_file)

# Save the character-based N-Grams to another JSON file as a list of lists
output_file_path_2 = "character_n_grams_test.json"
with open(output_file_path_2, 'w', encoding='utf-8') as output_file:
    json.dump({
        "top_20_unigrams": convert_ngrams_to_list(top_20_unigrams),
        "unigrams": convert_ngrams_to_list(char_unigrams),
        "top_20_bigrams": convert_ngrams_to_list(top_20_bigrams),
        "bigrams": convert_ngrams_to_list(char_bigrams),
        "top_20_trigrams": convert_ngrams_to_list(top_20_trigrams),
        "trigrams": convert_ngrams_to_list(char_trigrams)
    }, output_file, ensure_ascii=False, indent=4)
    
print("N-Gram generation completed and saved to file.")