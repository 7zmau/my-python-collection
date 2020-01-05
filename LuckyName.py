import random

def lucky(Name):
    if Name==1:
        return 'Aditya'
    if Name==2:
        return 'Khushboo'
    if Name==3:
        return 'Rohit'
    if Name==4:
        return 'Vrushank'
    if Name==5:
        return 'Chinmay'
    if Name==6:
        return 'Shivani'
    if Name==7:
        return 'Princeton'

r=random.randint(1, 7)
fortune=lucky(r)
print(fortune)
print(r)
