import string

def word_to_number(word):
    # Define a dictionary to map letters to their positions in the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_to_number = {letter: index + 1 for index, letter in enumerate(alphabet)}

    # Convert the word to uppercase and calculate the sum of letter positions
    word = word.upper()
    word_sum = sum(letter_to_number.get(letter, 0) for letter in word)

    return word_sum

while True:
    # Input word - Used to identify platform to be virtualized
    input_word = input("System name: ")

    # Check if the input word contains numbers
    if any(char.isdigit() for char in input_word):
        print("Numbers are not allowed in the word.")
    elif any(char in string.punctuation for char in input_word):
        print("Special characters are not allowed in the word.")
    else:
        # Calculate the sum
        word_sum = word_to_number(input_word)
        print(f"{input_word} = {word_sum}")

    another_conversion = input("Do you want to perform another conversion? (Y/N): ")
    if another_conversion.upper() != 'Y':
        break
