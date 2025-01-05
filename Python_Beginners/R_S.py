
P1=0
P2=0
count=0
while count<3:
    A_1 = input("Please enter your option :")
    A_2 = input("Please enter your option :")

    if A_1=="Rock" and A_2=="Scrissors":
        P1=P1+1
    elif A_1=="Scrissors" and A_2=="Rock":
        P2=P2+1
    elif A_1=="Paper" and A_2=="Scrissors":
        P2 = P2 + 1
    elif A_1=="Scrissors" and A_2=="Paper":
        P1=P1+1
    elif A_1=="Rock" and A_2=="Paper":
        P2=P2+1
    elif A_1 == "Paper" and A_2 =="Rock":
        P1=P1+1
    else:
        P1=P1+0
        P2=P2+0
    print(P1)
    print(P2)
    count = count + 1

if P1>P2:
     print("Congratulations Player 1 you won! ")
elif P2>P1:
    print("Congratulations Player 2 you won! ")

