#Iterators
a=['Hey','bro','ur','awesome']
for i in a:
    print(i)

print(dir(a))

#List iterator object
itr=iter(a)
print(itr)

#Go the next object in this list
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

# iterator through a list in reverse
itr2=reversed(a)
print(next(itr2))
print(next(itr2))
print(next(itr2))

#implement an iterator class
class RemoteControl():
    def __init__(self):
        self.channels=['HBO','CNN','abc','ESPN']
        self.index=-1

    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r=RemoteControl()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


#Exercise
class F():
    def __init__(self,limit):
        self.prev=0
        self.current=1
        self.n=1
        self.limit=limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n<self.limit:
            result=self.current+self.prev
            self.prev=self.current
            self.current=result
            self.n+=1
            return result
        else:
            raise StopIteration

# Init the fib_iterator

fib_iterator=iter(F(7))
while True:

    try:
        print(next(fib_iterator))

    except StopIteration:
        break

