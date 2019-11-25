import random

print ('Welcome to my Game!')
print ('Would you like to start')

userInput = input()

if (userInput == "Yes" or userInput == "yes"):
    print("Then let's get started, whats your Username?")
    name = input()
    print("Hello, " + name)
    print("Quick, a goblin has appeared! What spell will you use")
    print("Choose Fire or Ice")
    spell = input()
    if (spell == "Fire"):
        damage = random.randint(1, 5)
        print("You did " + damage + "damage")
else:
    print("Error, Wrong answer")
