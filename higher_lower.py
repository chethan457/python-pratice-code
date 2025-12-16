import gamedata
import random

print("lets start the game")

playerA= random.choice(gamedata.players)
game=True
rounds = 0
while game :

    #selecting player a
    print("Option A")

    print(f"{playerA['name']}, a {playerA['profession']}, from {playerA['from']}")
    
    #giving space
    print("\n\nv/s\n\n")

    #selecting player b
    similar = True
    while similar:
        print("Option B")
        playerB= random.choice(gamedata.players)
        if playerA != playerB:
            print(f"{playerB['name']}, a {playerB['profession']}, from {playerB['from']}")
            similar=False

    #getting user answer for a and b
    validinput=True
    while validinput:
        user_answer = input ("select one among both of the options. \nlike whom you think may have greater number of followers. \nenter a or b").lower()
        if user_answer in ["a", "b"]:
            validinput=False
        else:
            print("enter a valid input that is a or b")
            

    #getting actual answer

    if playerA["followers"]>playerB["followers"]:
        correct_answer = "a"
    elif playerB["followers"]>playerA["followers"]:
        correct_answer = "b"
    else:
        correct_answer = "a"  


    #declaring winner

    if user_answer == correct_answer:
        rounds+=1
        print(f"you made a correct guess.your score is {rounds} lets move to next guess")
        
    else:
        print("your guess was not correct. better luck next time")
        game=False

    if correct_answer == "b":
        playerA= playerB