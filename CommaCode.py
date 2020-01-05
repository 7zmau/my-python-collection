#Comma Code - wrote it on my own
#The function takes a list value as an argument and returns a string with all the items separated by a comma and space
#with 'and' inserted before the last item

def arrange(item1):
    print('''"''',end='')
    for i in item1[0:-2]:
        print(i, end=', ')
    print(item1[-2], end=' and ')
    print(item1[-1], end='''"''')

item=[]
while True:
    print("Enter item " + str(len(item) + 1) + ":" + " (Or press nothing to stop)")
    itemValues = input()
    if itemValues == '':
        break
    item = item + [itemValues]
if item == []:
    print("Enter some words to see the arrangement")
else:
    print("The list is: ", item)
    print("The arrangement is: ", end='')
    arrange(item)
    
