# list comprehension provides a was to
# transform one list into another
numbers=[1,2,3,4,5,6,7]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
        print(even)

#list comprehension
even2=[i for i in numbers if i%2==0]
print(even2)

sqr_numbers=[i**2 for i in numbers]
print(sqr_numbers)

#Set is unordered and it doesnt allow you
# to contain duplicate items.

s=set([1,2,3,4,5,2,3])
print(s)

even={i for i in numbers if i%2==0}
print(even)

even2={i for i in s if i%2==0}
print(even2)
# Creating a dictionary using dict comprehension

Cities=['Kumasi','Accra','Takoradi','Ho']
Regions=['Ashanti','Greater Accra','Western','Volta']
z=zip(Cities,Regions)
print(z)

for a in z:
    print(a)
#Dict Comprehension approach

d={city:region for city,region in zip(Cities,Regions)}
print(d)


#Exercise
Inte=[0,1,2,3,4,5]
binary=['0','1','10','11','100','101']

b=zip(Inte,binary)
print(b)

for i in b:
    print(i)

B_d={Integer:Binary for Integer,Binary in zip(Inte,binary)}
print(B_d)


integer=[1,-1,2,3,5,0,-7]
a_in={i*-1 for i in integer}
print(a_in)


integer2=[1,-1,2,-2,3,-3]
sq_set={i**2 for i in integer2}
print(sq_set)




