prodID=input("Enter product ID: ")
if prodID[0:2].isalpha():
    print("Authenticated")
else:
    print("Enter a valid product ID.")
    
