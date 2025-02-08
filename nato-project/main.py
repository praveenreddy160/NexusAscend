import pandas as pd

data = pd.read_csv("C:/Users/prave/nexusascend/nato-project/nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)
words = input("Enter a word: ").upper()
phonetic = [data_dict[letter] for letter in words]
print(phonetic)