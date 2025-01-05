#1
result=["heads",'tails','tails','heads','tails','heads','heads','tails','tails','tails']
for x in result:
    if x=="heads":
        h=len(x)
        print(h)

#2

Num= [1,2,3,4,5,6,7,8,9,10]

for i in Num:
    i=i**2
    print(i)

#3printing keys

M_exp={2340:"January",2500:'February',2100:"March",3100:"April",2980:"May"}
Mon=input('Please enter expense for the month :')
Mon=int(Mon)
for key in M_exp:
    if Mon in M_exp.keys():
        print(M_exp.get(Mon))
else:
    print("Unknown month")


#4
x=0
Race=[1,2,3,4,5]
for x in Race:
    x = x + 1
    if x<=5:
        F = input('Are you tired? :')
        if F=="Yes":
            r=5-x
            print("you didn't finish the race,",r,"km left")
            break


    elif F=="No":
        continue

else:
        print('Congratulations,you completed the race', )


#5
for S in range(1):
    print("*")
for T in range(1):
    print('**')
for J in range(1):
    print('***')
for J in range(1):
    print('****')
for J in range(1):
    print('*****')

















