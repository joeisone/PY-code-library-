def Div():
        Num = input("Please enter your number here :")
        Num = int(Num)
        Divisor=[]
        for i in range(1,Num+1):
                 if Num%i==0:
                    Divisor.append(i)
                    print(Divisor)

Div()




