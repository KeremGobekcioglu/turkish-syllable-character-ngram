def clean_text(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                # Strip leading and trailing whitespace (including newlines)
                stripped_line = line.strip()

                # Skip lines starting with <doc> or </doc>, and empty lines
                if stripped_line.startswith('<doc') or stripped_line.startswith('</doc') or not stripped_line:
                    continue

                # Convert the line to lowercase
                lower_line = stripped_line.lower()

                # Write the cleaned line to the output file
                output_file.write(lower_line + '\n')

# Call the function with your file paths
input_file_path = "turkish_wikipedia_dump\wiki_00"
output_file_path = "cleaned_wiki_00.txt"
clean_text(input_file_path, output_file_path)