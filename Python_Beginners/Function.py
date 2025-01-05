#1
def calculate_area_t(b,h):
    b = input('Please enter the base:')
    b = int(b)
    h = input('Please enter the height:')
    h = int(h)
    Area=(1/2)*b*h
    A=Area
    print(A)

#2
def calculate_area_r(l,w):
    l=input('Please enter the length :')
    l=int(l)
    w=input('Please enter the width :')
    w=int(w)
    R_area=l*w
    r= R_area
    print(r)


#Bas=input('Please enter the base:')
#b=int(Bas)
#Hei=input('Please enter the height:')
#h=int(Hei)
#A=calculate_area_t(b,h)
#print(A)


#2
#Note:for calling a functions, if you want to use the actual
#local variables of  the function call function in an if statment
#you simply put the arguments into bracket like below.

Area_option=input("Please enter the type of shape :")
A_0=str(Area_option)
if A_0 =="Triangle":
    calculate_area_t("b","h")
elif A_0=="Rectangle":
    calculate_area_r("l","w")
else:
    calculate_area_t("b","h")

#3
def print_pattern(Num):

    Num=int(Num)
    if Num==3:
        print("*")
        print("**")
        print("***")

    elif Num==4:
        print("*")
        print("**")
        print("***")
        print("****")

    else:
        print("Invalid")


Num=input("Please enter the integer number :")
print_pattern(Num)



