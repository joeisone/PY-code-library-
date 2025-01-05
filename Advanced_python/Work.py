class PowerTwo:
    def __init__(self,max):
        self.max=max

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<=self.max:
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
print(next(iterator3))

