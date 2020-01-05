name=input("Enter name: ")
if name=='Alice' or name=='alice' or name=='ALICE':
    age=int(input("Enter age: "))
    if ((age>12) and (age<=50)):
        print("Hi, Alice")
    elif age<=12:
        print("You are not Alice, kiddo")
    else:
        print("You are not Alice, old woman")
else:
    print("Only Alice.")
    
