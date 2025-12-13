import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player = 0
dealer = 0 


def pickinguser (player):
    
    pickingbyuser = random.choice(cards)
    player += pickingbyuser
    print("player picks a card")
    return player

def pickingdealer (dealer):
    
    pickingbydealer = random.choice(cards)
    dealer += pickingbydealer
    print("dealer picks a card")
    return dealer



print("Game starts all the best ")
player = pickinguser(player)
dealer = pickingdealer(dealer)
print(f"the total score of player is {player}")


while True:
    consent = input("do you wanna continue type y for yes and n for no").lower()

    if consent=="y":
        player= pickinguser(player)
        print(f"the total score of player is {player}")
        if player > 21:
            print("player lost")
            break

    elif consent == "n":
        while dealer<=17:
            dealer= pickingdealer(dealer)
            print(f"the total score of player is {player}")
            print(f"the total score of dealer is {dealer}")

        
        if dealer > player:
            print("dealer won")
        
        elif dealer < player:
            print("player won")

        elif player == dealer :
            print("draw")
        break
    





