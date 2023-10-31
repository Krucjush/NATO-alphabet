import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        print([nato_phonetic_alphabet_dictionary[letter] for letter in word])
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()


generate_phonetic()
