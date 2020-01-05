#Collatz Sequence Code
#Wrote the code without any reference so it took me some time
#You type in any integer and sooner or later it will arive with value 1 - Collatz Sequence

def collatz(number):
    if number % 2==0:
        return number //2
    elif number % 2==1:
        return 3*number+1

try:
    n=int(input("Enter number\n"))
    if n > 0:
        while n!=1:
            n=collatz(n)
            print(n)
    else:
        print("You must enter a positive integer")

except ValueError:
    print("You must enter an integer")


