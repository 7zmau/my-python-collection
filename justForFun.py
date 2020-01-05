import random
q = False
while not q:
    n = random.randint(10, 1000000)
    r = 7 ** n
    print("Result:\n", r)
    a = input("Continue? [Y/N]: ")
    if a == 'N' or a == 'n':
        q = True
    
