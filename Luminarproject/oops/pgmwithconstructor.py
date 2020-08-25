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


obj=Employee(1001,"rahul","ceo",50000)

obj.printValues()


#constructor

#the duty of constructor is initialize instance variables

#constructor automatically invoked during the time of object creation

#the name of constructor is always __init__(self)