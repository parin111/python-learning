import random
number = random.randint(1,20)
guess = int(input("guess a number from 1 to 20"))
while guess != number:
    if guess < number:
        print(number - guess)
        print("you are that many number(s) too less")
    else:
        print(guess - number)
        print("you are that many number(s) too much")
    guess = int(input("try again"))
    print("correct")
