N = int(input("How many numbers to sort?\n"))
A = []
for i in range(0,N):
    a = int(input("Enter number "+str(i+1)+':'))
    A.append(a)

for k in range(1,N):
    print('K='+str(k),',','A=',A)
    for j in range(0,N-k):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

print("Final list:",A)
