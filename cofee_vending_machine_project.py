#resource 'dictionary
resource={"Water": 1000 ,
"Milk": 500 ,
"Coffee": 760 ,
"Money": 2500 }

while True:
    type_of_drink= input("What kind of drink you need put exact letters to order \n1. latte \n2.capacino \n3.coffe \nenter off to off the coffee machine\n\n\n\n\n\n\n\n\n\n\n").lower()
    if type_of_drink=="report":
        for key , value in resource.items():
            print(f"{key} = {value}")
        continue
        
        
    elif type_of_drink == "off":
        exit()

    elif type_of_drink=="latte":

        print(f"You have requested for {type_of_drink}\n\n\n\n\n\n\n\n\n\n\n")

            #managingresource
        print ("you should pay 20rs")   
        payment1=int(input("how many10rs coins:"))*10
        payment2=int(input("how many5rs coins:"))*5
        payment3=int(input("how many2rs coins:"))*2
        payment4=int(input("how many1rs coins:"))*1
        payment=payment1+payment2+payment3+payment4
        if payment >= 20:
            returnchange = payment - 20
            if returnchange >0 :
                print(f"here is your change of{returnchange}")
        else:
            print(f"you should give 20rs. your paymwnt is not enough for you to provide {type_of_drink}\n\n\n\n\n\n\n\n\n\n\n")
            continue

        if resource["Water"]>=100 and resource["Coffee"]>=25 and resource["Milk"]>=50 :
            resource["Water"]-=100
            resource["Milk"]-=50
            resource["Coffee"]-=25
            resource["Money"]+=20
            print(f"Enjoy your {type_of_drink}\n Come back again")
        else:
            print("Sorry we dont have enough resource. we will serve you soon\n\n\n\n\n\n\n\n\n\n\n")
            continue
    elif type_of_drink == "capacino":
        print(f"You have requested for {type_of_drink}\n\n\n\n\n\n\n\n\n\n\n")

            #managingresource
        print ("you should pay 30rs")
        payment1=int(input("how many10rs coins:"))*10
        payment2=int(input("how many5rs coins:"))*5
        payment3=int(input("how many2rs coins:"))*2
        payment4=int(input("how many1rs coins:"))*1
        payment=payment1+payment2+payment3+payment4
        if payment >= 30:
            returnchange = payment - 30
            if returnchange >0 :
                print(f"here is your change of{returnchange}")
        else:
            print(f"you should give 30rs. your paymwnt is not enough for you to provide {type_of_drink}\n\n\n\n\n\n\n\n\n\n\n")
            continue

        if resource["Water"]>=200 and resource["Coffee"]>=50 and resource["Milk"]>=100 :
            resource["Water"]-=200
            resource["Milk"]-=100
            resource["Coffee"]-=50
            resource["Money"]+=30
            print(f"Enjoy your {type_of_drink}\n Come back again")
        else:
            print("Sorry we dont have enough resource. we will serve you soon\n\n\n\n\n\n\n\n\n\n\n")
            continue

    elif type_of_drink == "coffe":
        print(f"You have requested for {type_of_drink}\n\n\n\n\n\n\n\n\n\n\n")

        #managingresource
        print ("you should pay 10rs")  
        payment1=int(input("how many10rs coins:"))*10
        payment2=int(input("how many5rs coins:"))*5
        payment3=int(input("how many2rs coins:"))*2
        payment4=int(input("how many1rs coins:"))*1
        payment=payment1+payment2+payment3+payment4
        if payment >= 10:
            returnchange = payment - 10
            if returnchange >0 :
                print(f"here is your change of{returnchange}")
        else:
            print(f"you should give 10rs. your paymwnt is not enough for you to provide {type_of_drink}\n\n\n\n\n\n\n\n\n\n\n")
            continue

        if resource["Water"]>=50 and resource["Coffee"]>=15 and resource["Milk"]>=25 :
            resource["Water"]-=50
            resource["Milk"]-=25
            resource["Coffee"]-=15
            resource["Money"]+=10
            print(f"Enjoy your {type_of_drink}\n Come back again")
        else:
            print("Sorry we dont have enough resource. we will serve you soon\n\n\n\n\n\n\n\n\n\n\n")
            continue
    else:
        print("Please enter a valid option")