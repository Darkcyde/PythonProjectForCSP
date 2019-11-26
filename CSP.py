import random

# Fight function to ask for spell and attack enemy
def Fight():
    enemyHealth = 10
    

    while enemyHealth > 0:
        
        
        spell = input()
        if (spell == "Fire" or spell == "fire"):
            damage = random.randint(1, 5)
            enemyHealth = enemyHealth - damage
            print("You did", damage, "damage")
            print("the enemy has", enemyHealth, "health")
        else:
            print("Invalid spell!")

print ('Welcome to my Game!')
print ('Would you like to start')

userInput = input()

if (userInput == "Yes" or userInput == "yes" or userInput == "YEs"):
    print("Then let's get started, whats your Username?")
    name = input()
    print("Hello, " + name)
    print("Quick, a goblin has appeared! What spell will you use")
    
    enemyHealth = 10
    

    while enemyHealth > 0:
        
        print("Choose Fire or Ice")
        
        spell = input()
        if (spell == "Fire" or spell == "fire"):
            damage = random.randint(3, 5)
            enemyHealth = enemyHealth - damage
            print("You did", damage, "damage")
            print("the enemy has", enemyHealth, "health")
            
        elif (spell == "Ice" or spell == "ice"):
            damage = random.randint(1, 7)
            enemyHealth = enemyHealth - damage
            print("You did", damage, "damage")
            print("the enemy has", enemyHealth, "health")
            
        else:
            print("Invalid spell!")
        
    if (enemyHealth <= 0):
        print("You killed the witch!")
        print("Another one appears!")
        enemyHealth = 15
        Fight()
        
    if (enemyHealth <= 0):
        print("You killed the goblin!")
        print("Another one appears!")
        enemyHealth = 30
        Fight()

else:
    print("Error, Wrong answer")
    
print("Great job, you got a score of", score, "and beat my score")
