woman = ["a neurologist", "a clarvoyant", "a queen"]
man = ["a serial killer", "a stripper", "your grandfather"]
place = ["at a cave", "on an island"]
womansays = ["slay", "hurry up", "youre usless"]
mansays = ["sorry","please forgive me", "let me do that for you"]
consequences = ["rainbows", "a trip", "a swim"]
import random
while True:
    print(random.choice(woman), "met", random.choice(man), random.choice(place))
    print("she said", random.choice(womansays), "he says", random.choice(mansays))
    print("the consequence was", random.choice(consequences))
    

