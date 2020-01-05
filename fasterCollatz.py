def collatz(number):
    if number % 2==0:
        return number //2
    elif number % 2==1:
        return 3*number+1
n=int(input("Enter number\n"))
while n!=1:
    n=collatz(n)
    print(n)

