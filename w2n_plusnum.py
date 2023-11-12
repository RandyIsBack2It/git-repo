import string

def word_to_number(word):
    # Define a dictionary to map letters to their positions in the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_to_number = {letter: index + 1 for index, letter in enumerate(alphabet)}

    # Extend the dictionary to include numbers
    for digit in '0123456789':
        letter_to_number[digit] = int(digit)

    # Convert the word to uppercase and calculate the sum of letter positions and numbers
    word = word.upper()
    word_sum = 0
    current_number = ''
    for char in word:
        if char.isalpha():
            if current_number:
                word_sum += int(current_number)
                current_number = ''
            word_sum += letter_to_number.get(char, 0)
        elif char.isdigit():
            current_number += char
    if current_number:
        word_sum += int(current_number)

    return word_sum

while True:
    # Input word - Used to identify the platform to be virtualized
    input_word = input("System name: ")

    # Check if the input word contains special characters
    if any(char in string.punctuation for char in input_word):
        print("Special characters are not allowed in the word.")
    else:
        # Calculate the sum
        word_sum = word_to_number(input_word)
        # Display the result
        print(f"{input_word}")
        print(f"Sum = {word_sum}")

    another_conversion = input("Do you want to perform another conversion? (Y/N): ")
    if another_conversion.upper() != 'Y':
        break
