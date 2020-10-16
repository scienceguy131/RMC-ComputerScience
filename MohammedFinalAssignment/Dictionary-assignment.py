# Dictionary-assignment.py
# 420-GEB-03
# OCdt Al-Ansar Mohammed
# Copyright Mohammed 2020
# Description: Given a key text, forms a dictionary that can be used.
# also 'encrypts' messages using the code, starts with NATO alphabet
# Known limiations:

import sys


# input data/intial variables


nato_alphabet = "AlphaBravoCharlieDeltaEchoFoxtrotGolfHotelIndiaJuliettKilo\
LimaMikeNovemberOscarPapaQuebecRomeoSierraTangoUniformVictorWhiskeyX-ray\
YankeeZulu"


# function definitions


# given a text, converts each captial word into a value in a dictionary, using
# its starting letter as its key
# Testing: all types of strings, special characters, blank strings. Returns
# strings not in dictionary with square brackets around the character
def dictionary_maker(text):
    dictionary = {}
    for x in range(len(text)):

        if text[x].isupper():
            dictionary[text[x]] = text[x]
            for y in range(x+1, len(text)):

                if text[y].islower() or text[y] == "-":
                    dictionary[text[x]] = dictionary[text[x]] + text[y]

                else:
                    break

    return dictionary


# converts given texts using the dictionary
# Testing: all types of strings, special characters, blank strings. Returns
# strings not in dictionary with square brackets around the character
def convert_text(text, dictionary_func):
    converted_text = ""

    for i in range(len(text)):
        if text[i] == " ":
            converted_text += "[space] "

        else:
            try:
                converted_text += dictionary_func[text[i].upper()]
                if i != (len(text) - 1):
                    converted_text += " "   # leaves space at end
            except:
                converted_text += "[" + text[i] + "] "
    return converted_text


# starting menu that contains makes up the user inteface
# Testing: catches all unexpected input and creates error warning for
# user
def menu():

    print("*" * 10 + "Free text-code converter" + 10 * "*")
    dictionary = dictionary_maker(nato_alphabet)  # default dictionary

    while True:

        user_input = input("\nPlease select from one of the following options\
:\n\t1.Add new dictionary\n\t2.Use current dictionary to encrypt message\n\t\
3.Exit program\nEnter 1, 2, or, 3\n")
        print()

        if(user_input == "1"):
            user_dictionary = input("Please enter new data\n*NOTE:Data MUST be\
 formatted such that the key is the FIRST capitalized letter of the word(s), \
there are no spaces, and there are no duplicate first letters\n")

            try:
                dictionary = dictionary_maker(user_dictionary)
                print("Dictionary updated!")
                # print(dictionary) #to check errors
            except:
                print("ERROR please try again.\nBack to main menu:")
        elif(user_input == "2"):

            user_text = input("Please enter the text you would like to \
encrypt\n")
            new_text = convert_text(user_text, dictionary)
            print("Here is your new message:\n\n" + new_text + "\n")

        elif(user_input == "3"):

            print("Goodbye!")
            sys.exit(0)

        else:
            print("ERROR please select a valid entry.\nBack to main menu:")


# Main prg


menu()

sampleTuple = (1)
sampleDictionary = {1: "one"}
