# Exceptions are errors detected at the time of the program.
# road clear=Executing program without any exception.
# you identity the block of code
# which could possibly generate an issue and place
# try:  code   except  inbetween
x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=int(x)/int(y)
except Exception as e:
    print('exception occured: ', type(e).__name__)
    z=None
print("Division is: ", z)

