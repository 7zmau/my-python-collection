n = int(input("Enter the number of fibo to be generated:"))
i = 3
f1 = 1
f2 = 1
print(f1)
print(f2)
while i <= n:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    print(fn)
    i += 1

    
