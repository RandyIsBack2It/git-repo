from collections import Counter
import re
import os

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\w+', text.lower())  # Split text into words and convert to lowercase
        word_count = Counter(words)
        most_common = word_count.most_common(10)  # Change 10 to get more or fewer top words
        for word, count in most_common:
            print(f"{word}: {count}")

def list_files():
    files = os.listdir()  # List all files in the current directory
    print("Files in the current directory:")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

file_list = os.listdir()
print("Numbered list of files in the current directory:")
for i, file in enumerate(file_list, start=1):
    print(f"{i}. {file}")

file_index = int(input("Enter the number of the file you want to analyze: "))
if 1 <= file_index <= len(file_list):
    selected_file = file_list[file_index - 1]
    count_words(selected_file)
else:
    print("Invalid file number.")
