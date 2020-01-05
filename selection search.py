def findmin(A,i):
    loc = i
    for j in range(i+1,len(A)):
        if A[j] < A[loc]:
            loc = j
    return loc


N = int(input("How many numbers to sort?\n"))
A = []
for i in range(0,N):
    a = int(input("Enter number "+str(i+1)+':'))
    A.append(a)

for k in range(1,N):
    print('K='+str(k),',','A=',A)
    loc = findmin(A,k)
    temp = A[k]
    A[k] = a[loc]
    A[loc] = temp

print(A)
