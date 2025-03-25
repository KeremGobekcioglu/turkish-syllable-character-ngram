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

## 📄 Project Report

A detailed explanation of the project, methodology, and results can be found in the report:

📘 **[Turkish Language Modeling with N-Grams (PDF)](./Turkish%20Language%20Modeling%20with%20N%20Grams.pdf)**

This report covers:
- The motivation behind the project
- Data preprocessing and syllable segmentation
- N-gram generation for characters and syllables
- Evaluation metrics (e.g., perplexity)
- Results and analysis

We recommend reading it for a full understanding of the system.
