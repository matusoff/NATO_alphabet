# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


import pandas
#create dict from the csv file
data = pandas.read_csv(r'PROJECTS\100days_of_code\NATO_alphabet\NATO_phonetic_alphabet.csv')
#print(data.head())
#data_dict = data.to_dict()
#print(data_dict)

phonetic_alphabet = {row.letter : row.code for (index, row) in data.iterrows()}
#print(phonetic_alphabet)   

#using while loop
# game_is_on = True
# while game_is_on:
#     user_input = input("Enter a word: ").upper()

#     try:
#         new_code = [phonetic_alphabet[letter] for letter in user_input]
#         print(new_code)

#         if user_input == "Exit".upper():
#             game_is_on = False

#     except KeyError:
#         if user_input != phonetic_alphabet:
#             print("Sorry, only leters in the alphabet please")
        

#using function
def generate_phonetic():
    game_is_on = True
    while game_is_on:
        user_input = input("Enter a word: ").upper()
        if user_input == "Exit".upper():
                game_is_on = False

        try:
            new_code = [phonetic_alphabet[letter] for letter in user_input]
        
        except KeyError:
            print("Sorry, only leters in the alphabet please")
            generate_phonetic()
        
        else:
            print(new_code)

generate_phonetic()
    


