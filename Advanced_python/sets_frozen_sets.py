# set is an unordered collection of unique elements

basket={"orange","apple","mango","apple","orange"}
print(type(basket))
print(basket)

a=set()
a.add(1)
#b.add(2)
#As a programmer use set if you encounter
# lists that have duplicated and need to be sorted
numbers=[1,2,3,4,2,3,4]
unique_numbers={i for i in numbers}
print(unique_numbers)
#or
uni_numbers=set(numbers)
print(uni_numbers)
uni_numbers.add(5)
uni_numbers.add(6)
uni_numbers.add(7)
print(uni_numbers)

# Frozen set means you should not be able
# to change the content of set.
fs=frozenset(numbers)
print(fs)
#fs.add(5)

x={"a","b","c"}
print("a" in x)

y={'a','g','h'}
# To do a union use "|"
print(x|y)
#To return common element in both sets use "&"
print(x & y)
#To find a different "-"
print(x-y)

#If it is a subset see below
print(x<y)


#Exercise
num={1,2,3,4,5,6,7}
num2={2,3,5,2,6}
gg=frozenset(num)

print(num-num2)
print(num|num2)
print(num&num2)





