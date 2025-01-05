#Custom iterator in python

list1=[1,2,3,4,5]
iterator= iter(list1)
#Note:iter() is the function that would return the interator

print(next(iterator))
#next function
#this will return the first element in the list
print(next(iterator))
#this will return the Second element in the list
print(next(iterator))



#Using for loop
iterator2= iter(list1)
for element in iterator2:
    print(element,end=" ")
    #end=" " this ensure all the element will output be on the same line

#Note: When building an iterator from scartch it is easy in Python.
# We just have to implment the __iter__() and the __next__()
# methods:
#__iter__() returns the iterator object itself. If required, some initialization can be performed.

#__next__()must return the next item in the sequence. On reaching the end, and in subsequent calls, it
#it must raise StopIteration.

class PowerTwo:
    def __init__(self,max):
        self.max=max

    def __inter__(self):
        self.n=0
        return self

    def __next__(self):
        if (self.n<=self.max):
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration


i=PowerTwo(3)
iterator3=iter(i)
print(next(iterator3))
print(next(iterator3))
print(next(iterator3))