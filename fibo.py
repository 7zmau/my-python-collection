n=int(input("Enter number of terms: "))
t1=0
t2=1
print("Fibonacci Series:")
print(t1)
print(t2)
count=2
while count<n:
     display=t1+t2
     t1=t2
     t2=display
     count=count+1
     print(display)
     
     
