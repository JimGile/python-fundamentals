import random

roll = random.randint(1, 6)
guess = int(input('Guess the dice roll: \n'))

if guess == roll:
    print("Correct, computer rolled a " + str(roll))
else:
    print("The computer rolled a " + str(roll))
