#Decorators


import time


def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__+"took"+str(end-start)*1000)
        return result
    return wrapper

@time_it
def calc_Area_square():

    length=input("Please enter length :")
    breath=input("Please enter square :")
    length=int(length)
    breath=int(breath)
    square=length*breath

    print(square)
    return square

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number**3)

    print(result)
    return result

array=range(1,10)
#calc_Area_square()
#calc_cube(array)



