# For loop practise

# iterate over a list
names=['Jon','Mac','Ben','Joe']

for name in names:
    print(name)

# iterate over a string
word='Python'

for char in word:
    print(char)


# iterate over a range function

for i in range(10):
    print(i)

# iterate over tuple

Ghana=('Accra','Takoradi','Kumasi','Tamale')
for region in Ghana:
    print(region)

# iterate over a tuple of tuples
coordinates=[(1,2),(3,4),(5,6)]

for x,y in coordinates:
    print(f'x :{x},y :{y}')

# using enumerate for index and value
# enumerate prints the index values with the elements
names=['Jon','Mac','Ben','Joe']

for index, name in enumerate(names):
    print(f'Index {index}, Name:{name}')


#

