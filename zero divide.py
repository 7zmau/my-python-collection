def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument')

while True:
    m=spam(int(input("Enter a number to be divided by 42:")))
    if m is None:
        break
    print(m)
    
