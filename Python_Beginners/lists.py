#T1
#1
Total_exp={'January':2200,'February':2350,'March':2600,'April':2130,'May':2190}
Rev=Total_exp['February']%Total_exp['January']
print('In the month of February,',Rev,'more dollars were spent')

#2
Q_1=Total_exp["January"]+Total_exp["February"]+Total_exp["March"]
print('For the first quarter, the total expense is:',Q_1)

#3
if Total_exp==2000:
    print(Total_exp)
else:
    print('There is no month where expenses exceeded 2000')

#4 (To update dictionary)
Total_exp2={'June':1980}
Total_exp.update(Total_exp2)
print(Total_exp)



#5
Total_exp["April"]=Total_exp["April"]+200
print(Total_exp)

Refund=200
Total_exp["April"]=Total_exp["April"]+Refund
print(Total_exp)

#T2
Heros=['Spiderman','Batman','Superman','Ironman','Hulk','Captain America']

#1
print(len(Heros),'Super heros')

#2
Heros.append("Black panther")
print(Heros)

#3
Heros.remove("Black panther")
print(Heros)

Heros.insert(5,"Black panther")
print(Heros)

#4 Replacing in list
Heros[5:7]=['Doctor Strange']
print(Heros)

#5 Alphabetical order sorting of list
dir(Heros)
Heros.sort()
print(Heros)




