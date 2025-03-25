import random

def split_dataset(input_file_path, train_file_path, test_file_path, train_ratio=0.95):
    # Read the processed data from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Shuffle the lines to randomize the data (optional)
    random.shuffle(lines)

    # Calculate the split index
    split_index = int(len(lines) * train_ratio)

    # Split the data into training and testing sets
    train_data = lines[:split_index]
    test_data = lines[split_index:]

    # Save the training data to a new file
    with open(train_file_path, 'w', encoding='utf-8') as train_file:
        train_file.writelines(train_data)

    # Save the testing data to a new file
    with open(test_file_path, 'w', encoding='utf-8') as test_file:
        test_file.writelines(test_data)

    print(f"Data split complete. Training set: {len(train_data)} lines, Testing set: {len(test_data)} lines.")

# Example usage
input_file_path_1 = "syllable_based_model.txt"
train_file_path_1 = "syllable_based_model_train.txt"
test_file_path_1 = "syllable_based_model_test.txt"
split_dataset(input_file_path_1, train_file_path_1, test_file_path_1)

input_file_path_2 = "character_based_model.txt"
train_file_path_2 = "character_based_model_train.txt"
test_file_path_2 = "character_based_model_test.txt"
split_dataset(input_file_path_2, train_file_path_2, test_file_path_2)