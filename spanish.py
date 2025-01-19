import random


# Load dictionary from file
def load_dictionary(filename):
    dictionary = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            spanish, english = line.strip().split(' - ')
            dictionary[spanish] = english
            print(spanish)
    return dictionary




# Quiz in Spanish to English mode
def spanish_to_english(dictionary):
    words = list(dictionary.keys())
    random.shuffle(words)
    for word in words:
        print(f"Translate this word to English: {word}")
        user_input = input("Your answer: ")
        print(f"Correct translation: {dictionary[word]}\n")


# Quiz in English to Spanish mode
def english_to_spanish(dictionary):
    words = list(dictionary.items())
    random.shuffle(words)
    for spanish, english in words:
        print(f"Translate this word to Spanish: {english}")
        user_input = input("Your answer: ")
        print(f"Correct translation: {spanish}\n")


def main():
    # Load the dictionary
    filename = 'dictionary.txt'
    dictionary = load_dictionary(filename)

    # Choose quiz mode
    print("Choose mode: ")
    print("1. Spanish to English")
    print("2. English to Spanish")
    mode = input("Enter 1 or 2: ")

    if mode == '1':
        spanish_to_english(dictionary)
    elif mode == '2':
        english_to_spanish(dictionary)
    else:
        print("Invalid mode selected!")


if __name__ == "__main__":
    main()
