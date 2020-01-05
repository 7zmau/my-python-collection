n = int(input("Enter a number:"))
sumo = 0
while n != 0:
    r = n % 10
    n = n // 10
    sumo = sumo + r
print(sumo)
