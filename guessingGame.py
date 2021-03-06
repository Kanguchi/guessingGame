import random
number = random.randrange(1, 9)
#print(number)
userChance = 5
while(userChance>0 or userGuess!=number):
    userGuess = int(input("Guess a number from 1 to 9 : ")) 
    if(userGuess>number):
        print("Too high! Guess a number lower than", userGuess)
        userChance = userChance - 1
    elif(userGuess<number):
        print("Too low! Guess a number higher than", userGuess)
        userChance = userChance - 1
    elif(userGuess==number):
        print("Congratulations, YOU WON!")
if(userChance=0):
    print("YOU LOSE")
