# # # import string

# # # class Hececi:
# # #     def __init__(self):
# # #         self.sesliler = ["a", "e", "ı", "i", "o", "u", "ü", "ö"]
# # #         self.punctuation = set(string.punctuation)  # Set of punctuation characters

# # #     def hecelere_ayir(self, text):
# # #         kelime_dizisi = text.split()  # Split text into words
# # #         sonuc = []

# # #         # Process each word iteratively
# # #         for kelime in kelime_dizisi:
# # #             heceler = self._hecele(kelime)  # Get syllables of the word in correct order
# # #             sonuc.append(" ".join(heceler))  # Join syllables with ' '

# # #         return " ".join(sonuc)  # Return the processed text

# # #     def _hecele(self, sozcuk):
# # #         heceler = []
# # #         current_syllable = ""

# # #         for char in sozcuk:
# # #             if char in self.punctuation:
# # #                 if current_syllable:
# # #                     heceler.append(current_syllable)
# # #                     current_syllable = ""
# # #                 heceler.append(char)  # Treat punctuation as a separate syllable
# # #             else:
# # #                 current_syllable += char
# # #                 if self._sesli_var_mi(current_syllable):
# # #                     heceler.append(current_syllable)
# # #                     current_syllable = ""

# # #         if current_syllable:
# # #             heceler.append(current_syllable)

# # #         return heceler

# # #     def _sesli_var_mi(self, kelime):
# # #         return any(harf in self.sesliler for harf in kelime)


# # # # Function to read from file in chunks and write the syllable output incrementally
# # # def process_text_in_chunks(input_file_path, output_file_path, chunk_size=100000):
# # #     hececi = Hececi()
# # #     word_counter = 0  # To track the total number of words processed

# # #     with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
# # #         remainder = ""  # To store any leftover from the last chunk

# # #         while True:
# # #             chunk = input_file.read(chunk_size)
# # #             if not chunk:
# # #                 break  # Exit the loop if no more chunks to read

# # #             # Add the remainder from the last chunk to the current chunk
# # #             chunk = remainder + chunk

# # #             # Find the last complete word in the chunk
# # #             last_space = chunk.rfind(" ")
# # #             if last_space != -1:
# # #                 remainder = chunk[last_space + 1:]  # Save the remainder (the part after the last space)
# # #                 chunk = chunk[:last_space]  # Truncate the chunk to include only complete words

# # #             syllable_text = hececi.hecelere_ayir(chunk)
# # #             output_file.write(syllable_text + "\n")

# # #             # Update the word counter based on the number of words in the chunk
# # #             word_count_in_chunk = len(chunk.split())
# # #             word_counter += word_count_in_chunk

# # #             # Display progress every 1 million words
# # #             if word_counter % 1000000 < word_count_in_chunk:
# # #                 print(f"Processed {word_counter} words...")

# # #         # Process any remaining text after the loop ends
# # #         if remainder:
# # #             syllable_text = hececi.hecelere_ayir(remainder)
# # #             output_file.write(syllable_text + "\n")
# # #             word_counter += len(remainder.split())

# # #         print(f"Finished processing. Total words processed: {word_counter}")


# # # # Example usage
# # # input_file_path = "deneme.txt"
# # # output_file_path = "deneme_with_punc.txt"
# # # process_text_in_chunks(input_file_path, output_file_path)

# # import string

# # class Hececi:
# #     def __init__(self):
# #         self.sesliler = ["a", "e", "ı", "i", "o", "u", "ü", "ö", "A", "E", "I", "İ", "O", "Ö", "U", "Ü"]
# #         self.punctuation = list(string.punctuation)  # List of punctuation marks

# #     def hecelere_ayir(self, text):
# #         kelime_dizisi = []  # List to store words and punctuation

# #         # Process the text character by character
# #         temp_word = ""
# #         for char in text:
# #             if char in self.punctuation:
# #             # or char == " " or char == "\n":
# #                 # If the character is punctuation, space, or newline, treat it as a syllable
# #                 if temp_word:
# #                     kelime_dizisi.append(temp_word)  # Add the previous word
# #                     temp_word = ""  # Reset temp_word for next word

# #                 kelime_dizisi.append(char)  # Add punctuation, space, or newline as a "syllable"
# #             else:
# #                 temp_word += char  # Build the word syllable by syllable

# #         if temp_word:
# #             kelime_dizisi.append(temp_word)  # Append any remaining word

# #         sonuc = []
# #         for kelime in kelime_dizisi:
# #             if kelime in self.punctuation :
# #                 # or kelime == " " or kelime == "\n":
# #                 sonuc.append(kelime)  # If punctuation, space, or newline, add directly as a syllable
# #             else:
# #                 heceler = self._hecele(kelime)  # Get syllables of the word
# #                 sonuc.append(" ".join(heceler))  # Join syllables with space

# #         return " ".join(sonuc)  # Return the processed text

# #     def _hecele(self, sozcuk):
# #         heceler = []

# #         while len(sozcuk) > 0:
# #             if not self._sesli_var_mi(sozcuk):
# #                 if len(heceler) > 0:
# #                     # If the word has no more vowels, append the rest of the word to the last syllable
# #                     heceler[-1] += sozcuk
# #                 else:
# #                     heceler.append(sozcuk)
# #                 break

# #             # Find the position of the last vowel
# #             en_sagdaki_sesli_konumu = self._en_sagdakini_bul(sozcuk)

# #             # If the last vowel is at the beginning or followed by another vowel, form the syllable from it
# #             if en_sagdaki_sesli_konumu == 0 or self._sesli_mi(sozcuk[en_sagdaki_sesli_konumu - 1]):
# #                 hece = sozcuk[en_sagdaki_sesli_konumu:]
# #             else:
# #                 # Otherwise, include the consonant before the vowel as part of the syllable
# #                 hece = sozcuk[en_sagdaki_sesli_konumu - 1:]

# #             heceler.insert(0, hece)  # Insert syllables in the correct order
# #             sozcuk = sozcuk[:-len(hece)]  # Remove the processed syllable from the word

# #         return heceler

# #     def _en_sagdakini_bul(self, kelime):
# #         for i in range(len(kelime) - 1, -1, -1):
# #             if kelime[i] in self.sesliler:
# #                 return i
# #         return None

# #     def _sesli_mi(self, harf):
# #         return harf in self.sesliler

# #     def _sesli_var_mi(self, kelime):
# #         return any(self._sesli_mi(harf) for harf in kelime)


# # # Function to read from file in chunks and write the syllable output incrementally
# # def process_text_in_chunks(input_file_path, output_file_path, chunk_size=100000):
# #     hececi = Hececi()
# #     word_counter = 0  # To track the total number of words and syllables processed

# #     with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
# #         remainder = ""  # To store any leftover from the last chunk

# #         while True:
# #             chunk = input_file.read(chunk_size)
# #             if not chunk:
# #                 break  # Exit the loop if no more chunks to read

# #             # Add the remainder from the last chunk to the current chunk
# #             chunk = remainder + chunk

# #             # Find the last complete word in the chunk
# #             last_space = max(chunk.rfind(" "), chunk.rfind("\n"))  # Handle spaces and newlines
# #             if last_space != -1:
# #                 remainder = chunk[last_space + 1:]  # Save the remainder (the part after the last space or newline)
# #                 chunk = chunk[:last_space]  # Truncate the chunk to include only complete words/syllables

# #             syllable_text = hececi.hecelere_ayir(chunk)
# #             output_file.write(syllable_text + "\n")

# #             # Update the word counter based on the number of words and syllables in the chunk
# #             word_count_in_chunk = len(chunk.split())
# #             word_counter += word_count_in_chunk

# #             # Display progress every 1 million words/syllables
# #             if word_counter % 1000000 < word_count_in_chunk:
# #                 print(f"Processed {word_counter} words/syllables...")

# #         # Process any remaining text after the loop ends
# #         if remainder:
# #             syllable_text = hececi.hecelere_ayir(remainder)
# #             output_file.write(syllable_text + "\n")
# #             word_counter += len(remainder.split())

# #         print(f"Finished processing. Total words/syllables processed: {word_counter}")


# # # Example usage
# # input_file_path = "deneme.txt"
# # output_file_path = "deneme_with_punc.txt"
# # print("file name = " + output_file_path)
# # process_text_in_chunks(input_file_path, output_file_path)

# import string

# class Hececi:
#     def __init__(self):
#         self.sesliler = ["a", "e", "ı", "i", "o", "u", "ü", "ö", "A", "E", "I", "İ", "O", "Ö", "U", "Ü"]
#         self.punctuation = list(string.punctuation)  # List of punctuation marks

#     def hecelere_ayir(self, text):
#         kelime_dizisi = []  # List to store words and punctuation

#         # Process the text character by character
#         temp_word = ""
#         for char in text:
#             if char in self.punctuation:
#                 # If the character is punctuation, treat it as a syllable
#                 if temp_word:
#                     kelime_dizisi.append(temp_word)  # Add the previous word
#                     temp_word = ""  # Reset temp_word for next word

#                 kelime_dizisi.append(char)  # Add punctuation as a syllable
#             elif char not in [' ', '\n']:  # Ignore spaces and newlines
#                 temp_word += char  # Build the word syllable by syllable

#         if temp_word:
#             kelime_dizisi.append(temp_word)  # Append any remaining word

#         sonuc = []
#         for kelime in kelime_dizisi:
#             if kelime in self.punctuation:
#                 sonuc.append(kelime)  # If punctuation, add directly as a syllable
#             else:
#                 heceler = self._hecele(kelime)  # Get syllables of the word
#                 sonuc.append(" ".join(heceler))  # Join syllables with space

#         return " ".join(sonuc)  # Return the processed text

#     def _hecele(self, sozcuk):
#         heceler = []

#         while len(sozcuk) > 0:
#             if not self._sesli_var_mi(sozcuk):
#                 if len(heceler) > 0:
#                     # If the word has no more vowels, append the rest of the word to the last syllable
#                     heceler[-1] += sozcuk
#                 else:
#                     heceler.append(sozcuk)
#                 break

#             # Find the position of the last vowel
#             en_sagdaki_sesli_konumu = self._en_sagdakini_bul(sozcuk)

#             # If the last vowel is at the beginning or followed by another vowel, form the syllable from it
#             if en_sagdaki_sesli_konumu == 0 or self._sesli_mi(sozcuk[en_sagdaki_sesli_konumu - 1]):
#                 hece = sozcuk[en_sagdaki_sesli_konumu:]
#             else:
#                 # Otherwise, include the consonant before the vowel as part of the syllable
#                 hece = sozcuk[en_sagdaki_sesli_konumu - 1:]

#             heceler.insert(0, hece)  # Insert syllables in the correct order
#             sozcuk = sozcuk[:-len(hece)]  # Remove the processed syllable from the word

#         return heceler

#     def _en_sagdakini_bul(self, kelime):
#         for i in range(len(kelime) - 1, -1, -1):
#             if kelime[i] in self.sesliler:
#                 return i
#         return None

#     def _sesli_mi(self, harf):
#         return harf in self.sesliler

#     def _sesli_var_mi(self, kelime):
#         return any(self._sesli_mi(harf) for harf in kelime)


# # Function to read from file in chunks and write the syllable output incrementally
# def process_text_in_chunks(input_file_path, output_file_path, chunk_size=100000):
#     hececi = Hececi()
#     word_counter = 0  # To track the total number of words and syllables processed

#     with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
#         remainder = ""  # To store any leftover from the last chunk

#         while True:
#             chunk = input_file.read(chunk_size)
#             if not chunk:
#                 break  # Exit the loop if no more chunks to read

#             # Add the remainder from the last chunk to the current chunk
#             chunk = remainder + chunk

#             # Find the last complete word in the chunk
#             last_space = chunk.rfind(" ")
#             if last_space != -1:
#                 remainder = chunk[last_space + 1:]  # Save the remainder (the part after the last space)
#                 chunk = chunk[:last_space]  # Truncate the chunk to include only complete words/syllables

#             syllable_text = hececi.hecelere_ayir(chunk)
#             output_file.write(syllable_text + "\n")

#             # Update the word counter based on the number of words and syllables in the chunk
#             word_count_in_chunk = len(chunk.split())
#             word_counter += word_count_in_chunk

#             # Display progress every 1 million words/syllables
#             if word_counter % 1000000 < word_count_in_chunk:
#                 print(f"Processed {word_counter} words/syllables...")

#         # Process any remaining text after the loop ends
#         if remainder:
#             syllable_text = hececi.hecelere_ayir(remainder)
#             output_file.write(syllable_text + "\n")
#             word_counter += len(remainder.split())

#         print(f"Finished processing. Total words/syllables processed: {word_counter}")


# # Example usage
# input_file_path = "deneme.txt"
# output_file_path = "deneme_with_punc.txt"
# process_text_in_chunks(input_file_path, output_file_path)

import string
import re

class Hececi:
    def __init__(self):
        self.sesliler = ["a", "e", "ı", "i", "o", "u", "ü", "ö", "A", "E", "I", "İ", "O", "Ö", "U", "Ü"]
        self.punctuation = list(string.punctuation)  # List of standard punctuation marks

    def hecelere_ayir(self, text):
        kelime_dizisi = []  # List to store words, punctuation, and numbers

        # Process the text using regular expressions to extract words, numbers, and punctuation
        # This will match words, numbers, and any punctuation as separate tokens
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)

        for token in tokens:
            if token in self.punctuation:
                kelime_dizisi.append(token)  # Add punctuation as a syllable
            elif token.isdigit():
                kelime_dizisi.append(token)  # Add numbers as standalone syllables
            else:
                # Otherwise, process the word to extract syllables
                heceler = self._hecele(token)
                kelime_dizisi.append(" ".join(heceler))  # Join syllables with space

        return " ".join(kelime_dizisi)  # Return the processed text

    def _hecele(self, sozcuk):
        heceler = []

        while len(sozcuk) > 0:
            if not self._sesli_var_mi(sozcuk):
                if len(heceler) > 0:
                    # If the word has no more vowels, append the rest of the word to the last syllable
                    heceler[-1] += sozcuk
                else:
                    heceler.append(sozcuk)
                break

            # Find the position of the last vowel
            en_sagdaki_sesli_konumu = self._en_sagdakini_bul(sozcuk)

            # If the last vowel is at the beginning or followed by another vowel, form the syllable from it
            if en_sagdaki_sesli_konumu == 0 or self._sesli_mi(sozcuk[en_sagdaki_sesli_konumu - 1]):
                hece = sozcuk[en_sagdaki_sesli_konumu:]
            else:
                # Otherwise, include the consonant before the vowel as part of the syllable
                hece = sozcuk[en_sagdaki_sesli_konumu - 1:]

            heceler.insert(0, hece)  # Insert syllables in the correct order
            sozcuk = sozcuk[:-len(hece)]  # Remove the processed syllable from the word

        return heceler

    def _en_sagdakini_bul(self, kelime):
        for i in range(len(kelime) - 1, -1, -1):
            if kelime[i] in self.sesliler:
                return i
        return None

    def _sesli_mi(self, harf):
        return harf in self.sesliler

    def _sesli_var_mi(self, kelime):
        return any(self._sesli_mi(harf) for harf in kelime)


# Function to read from file in chunks and write the syllable output incrementally
def process_text_in_chunks(input_file_path, output_file_path, chunk_size=100000):
    hececi = Hececi()
    word_counter = 0  # To track the total number of words and syllables processed

    with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
        remainder = ""  # To store any leftover from the last chunk

        while True:
            chunk = input_file.read(chunk_size)
            if not chunk:
                break  # Exit the loop if no more chunks to read

            # Add the remainder from the last chunk to the current chunk
            chunk = remainder + chunk

            # Find the last complete word in the chunk
            last_space = chunk.rfind(" ")
            if last_space != -1:
                remainder = chunk[last_space + 1:]  # Save the remainder (the part after the last space)
                chunk = chunk[:last_space]  # Truncate the chunk to include only complete words/syllables

            syllable_text = hececi.hecelere_ayir(chunk)
            output_file.write(syllable_text + "\n")

            # Update the word counter based on the number of words and syllables in the chunk
            word_count_in_chunk = len(chunk.split())
            word_counter += word_count_in_chunk

            # Display progress every 1 million words/syllables
            if word_counter % 1000000 < word_count_in_chunk:
                print(f"Processed {word_counter} words/syllables...")

        # Process any remaining text after the loop ends
        if remainder:
            syllable_text = hececi.hecelere_ayir(remainder)
            output_file.write(syllable_text + "\n")
            word_counter += len(remainder.split())

        print(f"Finished processing. Total words/syllables processed: {word_counter}")


# Example usage
input_file_path = "cleaned_wiki_00.txt"
output_file_path = "syllable_based_model.txt"
process_text_in_chunks(input_file_path, output_file_path)
