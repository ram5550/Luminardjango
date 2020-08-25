class Employee:      #1001#rahul#ceo#50000
    # method
    def __init__(self,eid,ename,designation,salary):
        #the duty of setEmployee() intialize instance variables
        self.eid=eid
        self.ename=ename
        self.designation=designation
        self.salary=salary

    def printValues(self):
        print(self.eid)
        print(self.ename)
        print(self.designation)
        print(self.salary)

    def __str__(self):
        return self.ename

obj=Employee(1001,"rahul","ceo",50000)

print(obj)


