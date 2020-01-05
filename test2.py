catNames = []
while True:
    print("Enter item " + str(len(catNames) + 1) + ":" + " (Or press nothing to stop)")
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print("The cat names are:")
for name in catNames:
    print(' ' + name)
    
