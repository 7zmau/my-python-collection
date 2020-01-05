import math
num = int(input("Enter a number to calculate factorial of: "))
valid_input = False
while not valid_input:
    try:
        result = math.factorial(num)
        print("The factorial of", num, "is", result)
        valid_input = True
    except ValueError:
        print("Enter only a positive integer\n")
        num = int(input("Re-enter: "))
