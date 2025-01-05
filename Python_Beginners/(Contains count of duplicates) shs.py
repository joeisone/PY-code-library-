# Question 1
import csv
from typing import List,Dict
from itertools import chain

G=open("/Users/josephboateng/PycharmProjects/nyc_weather.csv","r")
reader=csv.reader(G)
# In order to move below the first line of csv file that are headers.
header = next(reader)
# To simple put csv file read into a list creating a 2D list.
datas=list(reader)
# This will simply convert your 1D list into a dictionary
FB=dict(datas)
print(FB)

Temp=input("Please enter the date: ")
Temp=str(Temp)
if Temp in FB.keys():
    J=FB.get(Temp)
    print("The temperature was:",J ,"degrees Celsuis")

# Question 2
# Counting duplicates elements in list
H=open("/Users/josephboateng/PycharmProjects/poem.txt",'r')
#  To read the whole text.
J=H.read()
print(J)
#This splits the whole word into
print(J.split())
A=J.split()
P=[]
for i, element in enumerate(A):
    print(i,element)

# This code counts the occurence of each element in the list
# and returns a dictionary
# This code generates the dictionary
# with the words and counts of occurance.
Q_list={i:A.count(i) for i in A}
print(Q_list)


# Chaining when there are two values or that
# have the same hashing function, the two
# values would be stored at the same key
# using a linked list

# Linear probing


