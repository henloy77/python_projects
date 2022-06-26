# phonetic letter conversionß
# Create a dictionary in this format:
import pandas
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict ={row.letter:row.code for (index,row) in alphabet_df.iterrows()}



# Create a list of the phonetic code words from a word that the user inputs.

response = input("Enter a word: ").upper()
response_list = [alphabet_dict[x] for x in response]
print(response_list)
