def split_text_to_characters(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for char in text:
            if char != ' ':
                output_file.write(char + ' ')
            else:
                output_file.write(char)

# Example usage
input_file_path = 'cleaned_wiki_00.txt'
output_file_path = 'character_based_model.txt'

split_text_to_characters(input_file_path, output_file_path)
print("Character-based model created successfully.")