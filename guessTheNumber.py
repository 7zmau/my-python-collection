import random
secretNumber=random.randint(1,20)
print("I'm choosing a number between 1 and 20")

for guessesTaken in range(1,7):
    guess=int(input("Take a guess \n"))

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break

if guess == secretNumber:
    print("Good Job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("The number I was thinking of was " + str(secretNumber))
