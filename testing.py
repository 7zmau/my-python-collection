def aloo(kyle):
    if kyle < 10:
        print("Less than 10")
    elif kyle == 10:
        print("Its 10")
    else:
        print("More than 10")
    sum1 = 9
    return sum1
    

n = int(input(("Enter a number: ")))
ans = aloo(n)
print(ans)
