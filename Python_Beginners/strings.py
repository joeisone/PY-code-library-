#1
Store_street= "Osu Oxford street, "
City="Accra, "
Country="Ghana. "
Address= Store_street+City+Country
print(Address)

#2
Statement='The earth revolves around the sun'
Char=len(Statement)
print(Char)
print(Statement[9:17])
print(Statement[-5:-1])

#3

F = input ('How many fruit do you consume a day: ')
V = input ('How many vegatables do you consume a day:')
print("I eat", F,"veggies and", V, " fruits daily")

#4 replacing incorrect words in string
s= "maine 200 banana khaye."
L= s.replace ("200","10").replace("banana","samosa")
print(L)
