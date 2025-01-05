#1
Country={"China":143,"India":136,"USA":32,"Pakistan":21}

Button=input("Please enter input :")
if Button=="Print":
    print("China==>143",
          "India==>136",
          "USA==>32",
          "Pakistan")
elif Button=="Add":
    A_d=input("Please enter the country name :")
    if A_d in Country:
        print("Sorry this country already exists")
    else:
        Country.update({A_d:35})
        print(Country)
elif Button=="Remove":
    D_d=input("Please enter the country that should be deleted :")
    D_d=str(D_d)
    if D_d in Country:
        Country.pop(D_d)
        print(Country)
    else:
        print("This country doesnt exist")

elif Button=="Query":
    Q_d=input("Which country do you want? :")
    Q_d=str(Q_d)
    if Q_d in Country.keys():
        A=Country.get(Q_d)
        print("The population is,", A,"million")

    else:
        print("Country not available")

#Note:dictionary name.pop

#2
def AVG():
    info = [600, 630, 620]
    ril = [1430, 1490, 1567]
    mtl = [234, 180, 160]
    Y=sum(info)/len(info)
    V=sum(ril)/len(ril)
    Z=sum(mtl)/len(mtl)

    print("info==>[600,630,620],==> AVG:",Y)
    print("ril==>[1430,1490,1560],==> AVG:",V)
    print("mtl==>[234,180,160]==>AVG:",Z)

info = [600, 630, 620]
ril = [1430, 1490, 1567]
mtl = [234, 180, 160]

O_O=input("Please enter your desired operations:")
if O_O=="Print":
       AVG()

elif O_O=="Add":
    T_T=input("Please enter stock ticker :")
    P_P = input("Please enter price :")
    P_P=int(P_P)
    if T_T =="info":
       info.append(P_P)
       print(info)
    elif T_T=="ril":
        ril.append(P_P)
        print(ril)
    elif T_T=="mtl":
        mtl.append(P_P)
        print(mtl)
    else:
        print(T_T,"==>",P_P)




#3
def circle_calc():
    r_d = input("Please enter the circle radius")
    r_d=int(r_d)
    PI=3.142
    Area=r_d*PI
    Circum=2*PI*r_d
    D_A=2*r_d
    print("Area is circle:",Area)
    print("Circumference of cricle:",Circum)
    print("Diameter of circle",D_A)

circle_calc()




    #else:
    #print("Unknown operation")





