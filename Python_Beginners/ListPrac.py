A=[1,4,9,16,25,36,49,64,81,100]
B=[]
for i in range(A[0],A[9]):
    if A[i]%2==0:
        B.append(A[i])
        print(B)
