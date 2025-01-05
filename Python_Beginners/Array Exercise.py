Exp=[2200,2350,2600,2130,2190]
#print("February expenses are",Exp[1])

#Q_1=Exp[0]+Exp[1]+Exp[2]
#print("Total expenses of first quarter",Q_1)

for i in range(len(Exp)):
    if Exp[i]==2000:
        print(Exp[i])
    else:
        print('There is no month you spent $2000')

Exp.append(1980)
print(Exp)


Exp[3]=Exp[3]-200
print(Exp)

Heros=['Spider man','Thor','Hulk','Iron man','Captain America']
print("Number of heros",len(Heros))

#Heros.append('Black panther')
#print(Heros)

Heros.insert(2,"Black panther")
print(Heros)

Heros.remove("Thor")
Heros.remove("Hulk")
print(Heros)

sorted(Heros)
Heros.sort()
#.sort() is used to present list in alphabetical order.
print(Heros)

O_D=[]

R_D=input("Please enter your number :")
R_D=int(R_D)

for i in range(1,R_D):
    if i%2==1:
        O_D.append(i)
print(O_D)