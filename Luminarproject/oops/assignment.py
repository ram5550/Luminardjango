#max salary

class Employee:      #1001#rahul#50000

    def __init__(self,eid,ename,salary):
        self.eid=eid
        self.ename=ename
        self.salary=salary

    def printValues(self):
        print(self.eid)
        print(self.ename)
        print(self.salary)

    def __str__(self):
        return self.ename

obj=Employee(1001,"rahul",50000)
obj1=Employee(1002,"ajay",35000)
obj2=Employee(1003,"vijay",33000)

ls=[]
ls.append(obj)
ls.append(obj1)
ls.append(obj2)

for employee in ls:
    if(employee.salary>35000):
        print(employee)





