import random

score = 0

# Level 1

goblinHealth = 20
damage = 0

print("A goblin has appeared")
print("What spell will you use?")


# whilst the enemy is alive:
while goblinHealth > 0:
    
    spellInput = input()
    
    if (spellInput == "Fire" or spellInput == "fire" or spellInput == "1"):
        
            damage = random.randint(3, 10)
            goblinHealth = goblinHealth - damage
            print("You damaged the Goblin for", damage, "damage and it is now", goblinHealth, "health")
            
    else:
        print("Wrong input")
        
# When the enemy is dead:
print("you killed the goblin great job!\n")
score = score + 1


# Level 2
witchHealth = 50
damage = 0

print("A witch has appeared")
print("What spell will you use?")

# whilst the enemy is alive:
while witchHealth > 0:
    
    spellInput = input()
    
    if (spellInput == "Fire" or spellInput == "fire" or spellInput == "1"):
        
            damage = random.randint(10, 30)
            witchHealth = witchHealth - damage
            print("You damaged the witch for", damage, "damage and she is now", witchHealth, "health")
            
    else:
        print("That's not a spell!")
        
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
    
    if (spellInput == "Fire" or spellInput == "fire" or spellInput == "1"):
        
            damage = random.randint(10, 50)
            dragonHealth = dragonHealth - damage
            print("You damaged the dragon for", damage, "damage and he is now", dragonHealth, "health")
            
    else:
        print("That's not a spell!")
        
# When the enemy is dead:
print("You killed the Dragon, good job!\n")
score = score + 1

print("You finished with a score of", score)
