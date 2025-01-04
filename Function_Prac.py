# Function pract

# I think of a function
# as a block of reusable
# code.

# singing happy birthday
# three times

# function that prints Happy birthday to
# specific name based on a specific number of times.

def birthday(name,age,times):
    counter=0
    while times!=0:
        print(f"Happy birthday {name}!,"
              f"you are {age} years old!")
        counter+=1
        if counter==times:
            break

birthday('Joseph',30,3)

# Function to display an invoice

def display_invoice(username,amount,due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}')

display_invoice('Joe is one',10000,'2nd February 2024')

# return is a statement used to end a function
# and send a result back to the caller.

def add(x,y):
    z=x+y
    return z

def substract(x,y):
    g=x-y
    return g

def multiply(x,y):
    f=x*y
    return f

def divide(x,y):
    d=x/y
    return d

def exp(x,y):
    s=x**y
    return s

z= add(1,2)
print(z)

print(exp(3,5))

# function to capitalise first letter
# of first and last name.

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+ " "+last

full_name=create_name('joseph','boateng')
print(full_name)
