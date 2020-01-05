n = 0
def call(num):
    for i in range(2, 1002, 2):
        num = num + 2
        return num
choco = call(n)
if choco == 1000:
    print("That's right man!")
    print("Enter a number:")
    n = input()
    call(n)
