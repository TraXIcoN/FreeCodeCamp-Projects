# APP 1
# DICTONARY
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dec(w):
    w = w.lower()
    if w in data:
        return data[w]                      # [] have been used in order to function as a ditonary 
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn =  input(f"Did you mean {get_close_matches(w,data.keys())[0] } insted? \n Enter Y if yes and N if no : ")
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" :
            ynn=  input(f"Did you mean {get_close_matches(w,data.keys())[1] } insted? \n Enter Y if yes : ")
            if ynn == "Y":
                return data[get_close_matches(w,data.keys())[1]]
            else:
                print(" We didn't understand your entry. ") 
            
        else:
            print(" We didn't understand your entry. ")
    else:
        print("word does not exist. ")

word = input(" enter a word :")
output = dec(word)
if type(output) == list:
    for i in output:
        print(i)


