import string

def word_to_number(word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_to_number = {letter: index + 1 for index, letter in enumerate(alphabet)}

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
    input_word = input("System name: ")

    if any(char in string.punctuation for char in input_word):
        print("Special characters are not allowed in the word.")
    else:
        word_sum = word_to_number(input_word)

        if word_sum > 255:
            excess_characters = word_sum - 255
            print(f"The sum of {input_word} is {excess_characters} characters over the limit of 255. Please try something else.")
        else:
            print(f"{input_word}")
            print(f"Sum = {word_sum}")

    another_conversion = input("Do you want to perform another conversion? (Y/N): ")
    if another_conversion.upper() != 'Y':
        break
