India=['Mumbai','Bangalore','Chennai','Delhi']
Pakistan=['Lahore','Karachi','Islamabad']
Bangladesh=["Dhaka",'Khulna','Rangpur']

#1
City_name= input("Please enter your City name :")
if City_name in India:
    print (City_name, "is a City in India")
elif City_name in Pakistan:
    print (City_name, "Is a city in Pakistan")
elif City_name in Bangladesh:
    print (City_name, "is a city in Bangladesh")
else:
    print("This city is unknown")


#2
City_name2= input("Please enter your City name :")
City_name3= input("Please enter your City Name :")
if City_name2 in India and City_name3 in India:
    print(City_name3, "and", City_name3, "are both in India")
elif City_name2 in Pakistan and City_name3 in Pakistan:
    print(City_name2, "and", City_name3, "are both in Pakistan")
elif City_name2 in Bangladesh and City_name3 in Bangladesh:
    print(City_name2, "and", City_name3, "are both in Bangladesh")
else:
    print ("Cities are unknown")

#T2
#3


F_Sugar_level=input("Please enter your fasting sugar level :")
F_Sugar_level=int(F_Sugar_level)
if F_Sugar_level >=80 and F_Sugar_level<=100:
    print(F_Sugar_level,"is within the normal fasting level sugar")
elif F_Sugar_level<80:
    print(F_Sugar_level,"sugar level is low")
elif F_Sugar_level>100:
    print(F_Sugar_level, "sugar level is high")
else:
    print("Sugar level unknown")
