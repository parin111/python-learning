exitChoice = "nothing"
while exitChoice != "EXIT":
    cats = 5
    password = "CATS"
    print("save world from cats")
    guess = input("guess the password").upper()
    while guess != password:
        print("password incorrect")
        cats = cats * 5
        print("there are now", cats, "cats on earth")
        if cats > 5500:
            break
        guess = input("guess again").upper()
    if cats > 5500:
        print("cats won")
    else:
        print("humans won")
    exitChoice = input("write exit if you wish to exit").upper

