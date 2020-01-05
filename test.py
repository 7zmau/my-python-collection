def arrange(item1):
    for i in item1[0:-2]:
        print(i, end=', ')
    print(item1[-2], end=' and ')
    print(item1[-1])

item=[]
while True:
    itemValues = input(print("Enter item " + str(len(item)) + ":" + " (Or press nothing to stop)"))
    if itemValues =='':
        break
    item = item + [itemValues]
if item == []:
    print("You must enter some words to see the arrangement")
else:
    arrange(item)    
    
    
