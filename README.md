# Turkish Syllable and Character N-Gram Language Modeling

This repository contains Python scripts for generating and analyzing character- and syllable-based n-gram models for the Turkish language.

## 📁 Project Structure

- `count_character.py`: Generate character n-grams
- `count_syllable.py`: Generate syllable n-grams
- `split_train_test.py`: Train/test split logic
- `treat_punc_syllable.py`: Punctuation and syllable preprocessing
- `turing_perplexity_sentence.py`: Perplexity calculation based on n-grams
- `cleaning/`: Optional post-processing or experimental cleaning steps

## 🧠 Dataset

The data used for this project is from the **[Turkish Wikipedia Dump on Kaggle](https://www.kaggle.com/datasets/mustfkeskin/turkish-wikipedia-dump)**.

Big thanks to [Mustafa Keskin](https://www.kaggle.com/mustfkeskin) for sharing the dataset.

## 📦 Note on Data Files

The generated `.json` files for n-gram counts are **excluded** from this repository due to their large size.