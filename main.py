import pandas
#create dict from the csv file
data = pandas.read_csv(r'file path \NATO_phonetic_alphabet.csv')

phonetic_alphabet = {row.letter : row.code for (index, row) in data.iterrows()}   

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
    


