class Employee:
    def __init__(Employee,ID,Name):
        Employee.ID=ID
        Employee.Name=Name
E1=Employee(1,"Joseph")
E2=Employee(2,"Coder")
print("Name:",E1.Name)
print("ID:",E1.ID)
print("Name:", E2.Name)
print("ID:",E2.ID)
#Below is the code to delete property from the object
del E2
#Below checks if E2 has been deleted it should return an error of undefined
print("Name:", E2.Name)
print("ID:",E2.ID)


