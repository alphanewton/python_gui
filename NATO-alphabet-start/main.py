import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_phrase = input("Enter a word: ").upper()
    try:
        l1 = [phonetic_dict[i] for i in user_phrase]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(l1)


generate_phonetic()
