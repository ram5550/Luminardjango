from functools import *
class Employee:
    def __init__(self,id,name,desig,salary):

        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def printEmp(self):
        print("name",self.name)
        print("designation",self.desig)
        print("salary",self.salary)
    def __str__(self):
        return self.name


f=open("edetails","r")

emplst=[]
for data in f:
    "100,sree,centerhead,50000"

    values=data.rstrip("\n").split(",")

    id=values[0]
    name=values[1]
    desig=values[2]
    salary=values[3]
    obj=Employee(id,name,desig,salary)
    emplst.append(obj)



salary=list(map(lambda employee:employee.salary,emplst))
print(salary)

maxsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salary)
print(maxsal)

maxsalemp=list(filter(lambda employee: employee.salary==maxsal,emplst))

for emp in maxsalemp:
    print(emp)