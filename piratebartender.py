import random
import sys

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

answers = {
}

drink = []

def ask():
    """I ask a series of questions to find out what drink you want"""
    response = input(questions["strong"])
    if response == 'y' or response == 'yes' or response == 'YES' or response == "Yes":
        answers["strong"] = True
    else:
        answers["strong"] = False
    response = input(questions["salty"])
    if response == 'y' or response == 'yes' or response == 'YES' or response == "Yes":
        answers["salty"] = True
    else:
        answers["salty"] = False
    response = input(questions["bitter"])
    if response == 'y' or response == 'yes' or response == 'YES' or response == "Yes":
        answers["bitter"] = True
    else:
        answers["bitter"] = False
    response = input(questions["sweet"])
    if response == 'y' or response == 'yes' or response == 'YES' or response == "Yes":
        answers["sweet"] = True
    else:
        answers["sweet"] = False
    response = input(questions["fruity"])
    if response == 'y' or response == 'yes' or response == 'YES' or response == "Yes":
        answers["fruity"] = True
    else:
        answers["fruity"] = False
    return answers
        
def makedrink(answers):
    """I make a drink in response to collected answers"""
    if answers["strong"] == True:
        drink.append(random.choice(ingredients["strong"]))
    if answers["salty"] == True:
        drink.append(random.choice(ingredients["salty"]))
    if answers["bitter"] == True:
        drink.append(random.choice(ingredients["bitter"]))
    if answers["sweet"] == True:
        drink.append(random.choice(ingredients["sweet"]))
    if answers["fruity"] == True:
        drink.append(random.choice(ingredients["fruity"]))
    return "Your drink is served: " + str(drink)
    
if __name__ == '__main__':
    answers = ask()
    drink = makedrink(answers)
    print(drink)
