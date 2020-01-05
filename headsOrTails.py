import random, sys
while True:
    print("I'm going to toss a coin.")
    element = random.randint(1,2)
    guess = input(("Take a guess. Enter 'H' for Heads and 'T' for Tails. Enter 'q' to quit: "))
    if guess == 'H' or guess == 'h' or guess == 'Heads' or guess == 'heads' or guess == 'Head' or guess == 'head':
        store = 1
    elif guess == 'T' or guess=='t' or guess == 'Tails' or guess == 'tails' or guess == 'Tail' or guess == 'tail':
        store = 2
    elif guess == 'q':
        sys.exit()
    else:
        a = input("Invalid input. Enter any key to continue. Enter 'q' to quit.")
        if a == 'q':
            sys.exit()
        else:
            print('\n\n')
            continue
    if store:
        if store == 1:
            if store == element:
                print("You guessed right! It's heads.")
            else:
                print("Nah.. It's tails.")
        elif store == 2:
            if store == element:
                print("You guessed right! It's tails.")
            else:
                print("Nah.. It's heads.")
        last = input("Wanna play again? If yes, enter any key to continue. Enter 'q' to quit.")
        if last == 'q':
            sys.exit()
        else:
            print('\n\n')
            continue

        
        

