a=[1,1,2,3,5,8,13,21,34,55,89]
b=[]
c=[]
for i in a:
    if i<5:
        b.append(i)
        print("The following are less than 3 :",b)
    else:
        c.append(i)
        print("The following are greater that 3: ",c)
