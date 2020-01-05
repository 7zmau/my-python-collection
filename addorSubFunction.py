def add():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    return a+b
def sub():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if a>b:
        return a-b
    else:
        return b-a
    
    
while True:
    x=input("Enter '1' to add or '2' to subtract or '3' to exit:\n")
    if x=='':
        print("I'm leaving!")
        break
    elif x=='1':
        num = add()
        print("The sum is", num)
        continue
    elif x=='2':
        num = sub()
        print("The difference is",num)
        continue
    elif x=='3':
        break
    else:
        print("Invalid choice!")
        continue
    
    
      
    
