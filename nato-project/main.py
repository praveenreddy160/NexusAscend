import pandas as pd

def file_mechanishm():
    # Read the CSV file into a DataFrame
    data = pd.read_csv("C:/Users/prave/nexusascend/nato-project/nato_phonetic_alphabet.csv")
    
    # Create a dictionary from the DataFrame
    data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    
    # Get user input and convert it to uppercase
    words = input("Enter a word: ").upper()
    
    try:
        # Create a list of phonetic codes for each letter in the input word
        phonetic = [data_dict[letter] for letter in words]
    except KeyError:
        # Handle the case where the input contains non-alphabet characters
        print("Sorry, only letters in the alphabet please.")
    else:
        # Print the list of phonetic codes
        print(phonetic)
        
file_mechanishm()