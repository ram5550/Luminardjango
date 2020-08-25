class Employee:
    def __init__(self,id,name,desig,salary):

        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def printEmp(self):
        print("name",self.name)
        print("designation",self.desig)
        print("employee salary",self.salary)

    def __str__(self):
        return self.name

f=open("details","r")

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

upper=list(map(lambda employee: employee.name.upper(),emplst))
print(upper)


salary=list(map(lambda employee: int(employee.salary)+5000,emplst))
print(salary)

maxsalary=list(filter (lambda employee: int(employee.salary)>30000,emplst))

for i in maxsalary:
    print("salary greater than 30000",i)