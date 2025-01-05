# multithreading is the process of handling more than one
# thread (task) at the same time.
#Example
# Given a list of numbers print the square of the numbers and print the cube of numbers

import time

def calSquare(numbers):
    print("Calculate square numbers")
    for n in numbers:
        n=n**2
        time.sleep(0.2)
        print('Square',n)

def calCube(numbers):
    print('Calculate the cube of numbers')
    for n in numbers:
        n=n**3
        time.sleep(0.2)
        print('square',n)

arr=[2,3,4,5]
t=time.time
calSquare(arr)
calCube(arr)


print(time.time())

#multithreading

import threading


def calSquare(numbers):
    print("Calculate square numbers")
    for n in numbers:
        n=n**2
        time.sleep(0.2)
        print('Square',n)

def calCube(numbers):
    print('Calculate the cube of numbers')
    for n in numbers:
        n=n**3
        time.sleep(0.2)
        print('square',n)

arr=[2,3,4,5]
t=time.time
t1=threading.Thread(target=calSquare,args=(arr,))
t2=threading.Thread(target=calCube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()
print(time.time())

#Exercise

for i in range(10):
    th=threading.Thread(target=calSquare,args=(i,arr))
    th2=threading.Thread(target=calCube,args=(i,arr))
    print(th)
    print(th2)

th3=threading.active_count()
print(th3)


def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):
    th = threading.Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())