import random

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

def ask():
    """I ask a series of questions to find out what drink you want"""
    answers = {}
    for type, question in questions.items():
        response = input(questions[type])
        if response.lower() == 'y' or response.lower() == 'yes':
            answers[type] = True
        else:
            answers[type] = False
    return answers
        
def makedrink(answers):
    """I make a drink in response to collected answers"""
    drink = []
    
    for type, liked in answers.items():
        if not liked:
            continue
        drink.append(random.choice(ingredients[type]))

    print("Your drink is served: ")
    for ingredient in drink:
        print("A {}".format(ingredient))
        
    return drink
    
if __name__ == '__main__':
    answers = ask()
    drink = makedrink(answers)