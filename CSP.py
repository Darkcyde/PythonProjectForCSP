import random
from colorama import Fore, Back, Style 

#On start:

print("What is your favorite color (RGB only :(")
color = input()

# Make this a switch statment***
if (color == "Red" or color == "RED"):
    print(Fore.RED + "Your text will now be Red!")
elif (color == "Blue" or color == "BLUE"):
    print(Fore.BLUE + "Your text will now be Blue!")
elif (color == "Green" or color == "GREEN"):
    print(Fore.GREEN + "Your text will now be Green!")

i = 0
score = 0

# Level 1

goblinHealth = 20
damage = 0

print("A goblin has appeared")
print("What spell will you use?")


# whilst the enemy is alive:
while goblinHealth > 0:
    
    spellInput = input()
    i += 1
    
    if (i < 10):
        if (spellInput == "Fire" or spellInput == "fire" or spellInput == "1"):
            
            damage = random.randint(5, 8)
            goblinHealth = goblinHealth - damage
            print("You damaged the Goblin for", damage, "damage and it is now", goblinHealth, "health")
            
        elif (spellInput == "Ice" or spellInput == "ice"):
            damage = random.randint(1, 10)
            goblinHealth = goblinHealth - damage
            print("You damaged the Goblin for", damage, "damage and it is now", goblinHealth, "health")
            
        else:
            print("Wrong input")
    
    else:
        print("You died!")
        
# When the enemy is dead:
print("you killed the goblin great job!\n")
score = score + 1


# Level 2
witchHealth = 50
damage = 0
i = 0

print("A witch has appeared")
print("What spell will you use?")

# whilst the enemy is alive:
while witchHealth > 0:
    
    spellInput = input()
    i += 1
    
    if (i < 5):
        if (spellInput == "Fire" or spellInput == "fire" or spellInput == "1"):
            
                damage = random.randint(10, 30)
                witchHealth = witchHealth - damage
                print("You damaged the witch for", damage, "damage and she is now", witchHealth, "health")
                
        else:
            print("That's not a spell!")
            
    else:
        print("You died!")
        
# When the enemy is dead:
print("You killed the witch, good job!\n")
score = score + 1

#Level 3 Boss fight
dragonHealth = 100
damage = 0

print("The mighty dragon has appeared")
print("What spell will you use?")

# whilst the enemy is alive:
while dragonHealth > 0:
    
    spellInput = input()
    i += 1
    
    if (i < 7):
        if (spellInput == "Fire" or spellInput == "fire" or spellInput == "1"):
            
                damage = random.randint(10, 50)
                dragonHealth = dragonHealth - damage
                print("You damaged the dragon for", damage, "damage and he is now", dragonHealth, "health")
                
        else:
            print("That's not a spell!")
    
    else:
        print("You died!")
        
# When the enemy is dead:
print("You killed the Dragon, good job!\n")
score = score + 1

print("You finished with a score of", score)

