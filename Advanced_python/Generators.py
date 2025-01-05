# Generators is a simple way of
# creating an iterator

def remote_control_next():
    yield "cnn"
    yield "espn"
# Yield returns a generator object
itr=remote_control_next()
print(itr)
print(next(itr))
print(next(itr))

for c in remote_control_next():
    print(c)

# Fibonacci sequence: 0,1,1,2,3,5,8,13,21,34,55
# Produce fibonacci using a generator

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if f>50:
        break
    print(f)

#Benefits
# You dont need to define iter and next
# you dont need to raise stop iteration exception

#Excercise

def Square():
    a=1
    i=0
    while 1 <= 100:
        i+=1
        a = a ** 2
        yield a
        a=i+1

#for i in Square():
   # if i>=10:
       # break
   # print(i)

itr2=Square()
print(itr2)
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))

