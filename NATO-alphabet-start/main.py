import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
print([nato_phonetic_alphabet_dictionary[letter] for letter in word])
