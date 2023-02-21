import random
exitChoice = "Nothing"
while exitChoice != "exit":
    player_choice = input("choose number 1, 2,3 or 4")
    if player_choice == "1":
        print("g")
    elif player_choice == "2":
        print("you enter the room with a sphinx")
        print("it asks you to guess what number it is thinking of, between 1 and 10")
        number = int(input("what number do you choose"))
        if number == random.randint(1,10):
            print("sphinx is dissapointed.youre correct")
        else:
            print("youre incorrect")

    elif player_choice == "3":
        print("hi")
    elif player_choice == "4":
        print("hello")
    else:
        print("you didnt type 1,2,3 or4")
    exitChoice = input("press return to play again or type exit to leave")
    
