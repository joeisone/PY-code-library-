def Pali():
    Q = input("Please enter the word :")
    # The code below is for returning the reverse of a string
    Q_2= Q[::-1]
    if Q==Q_2:
        print("This word",Q,"is a palindrome")
    else:
        print("This word",Q,"is not a palindrome")

Pali()
