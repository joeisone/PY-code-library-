# javascript object notation
import json

book={}
book['bob']={
    'name':'bob igor',
    'Date':'6 June 2024',
    'Salary':14000
}

book['joe']={
    'name':'joe',
    'Date':'5 June 2024',
    'Salary':15000
}

s=json.dumps(book)
#dumping as a string in JSON format
print(s)
print(type(s))
p=open("/Users/josephboateng/PycharmProjects/json.txt","w")
p.write(s)