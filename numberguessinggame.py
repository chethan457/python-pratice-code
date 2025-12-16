import random

print ("Welcome to the number guessing game:")
secretnumber = random.randint(1,100)

difficult_level= input("What level of game do you wanna play enter easy or hard").lower()
won = False
if difficult_level == "easy":
    for i in range(10,0,-1):
        guessed_number=int(input(f"you have {i} attempts left: \nguess the number: "))
        if guessed_number > secretnumber:
            print("too high. make another guess")
        if guessed_number<secretnumber:
            print("too low. make another guess")
        if guessed_number == secretnumber:
            print("you made a correct guess. you won")
            won=True
            break

    


if difficult_level == "hard":
    for i in range(5,0,-1):
        guessed_number=int(input(f"you have {i} attempts left: \nguess the number: "))
        if guessed_number > secretnumber:
            print("too high. make another guess")
        if guessed_number<secretnumber:
            print("too low. make another guess")
        if guessed_number == secretnumber:
            print("you made a correct guess. you won")
            won=True
            break


if not won:
    print("you could not guesss this number \n you lost")
        

