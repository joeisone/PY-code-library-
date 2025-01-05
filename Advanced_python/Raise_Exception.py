# Defining a class for exceptions
class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print('User defined exception:',self.msg)

try:
    raise Accident('Crach between two cars')
except Accident as e:
    e.print_exception()


class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def handle(self):
        print('accident occured. Take detour',self.msg)

try:
    raise Accident('Crach between two cars')
except Accident as e:
    e.handle()


#Generic
try:
    raise MemoryError('memory error')

except Exception as e:
    print(e)

#Specific
try:
    raise MemoryError('memory error')

except MemoryError as e:
    print(e)

# Finally statement
#def process_file():
    #try:
       #f=open("c://code//data.txt")
        #x=1/0
    #except FileNotFoundError as e:
        #print("inside except")
    #finally:
       # print("cleaning up file")
       # f.close()

# process_file()

# Exercise
class AdultException(Exception):
    def __init__(self,msg):
        self.msg=msg

    def handle(self):
        print("The person is underage")

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_minor_age(self,age):
        if int(age)>=17:
            print("Person is major")

        else:
            raise AdultException ("Person is under the age limit and is a minor")



    def display_person(self,name,age):
        print(name)
        print(f'The age of {name}, is {age}')
        print(self.get_minor_age(19), self.name)


P=Person('Samuel',12)
P.display_person('Samuel',18)






