import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
data.iterrows()

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def start_loop():
    name = input("Type in a name to get NATO alphabet for: ").upper()
    try:
        nato_list = [alphabet_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters are acceptable")
        start_loop()
    else:
        print(nato_list)


start_loop()
