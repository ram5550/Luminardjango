class Person:
    def setValues(self,personname,age):
        self.personname=personname
        self.age=age

    def printValues(self):
        print(self.personname)
        print(self.age)


class Bank(Person):
    bname="SBK"  #static variable
    def __init__(self,accno):
        self.accno=accno
        self.balance=3000


    def withdraw(self,amount):

        if(amount>self.balance):
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print("Remaining balance is",self.balance)

    def deposit(self,amount):
        self.balance+=amount
        print("Remaining balance is",self.balance)

    def balaceEnquiry(self):
        print("Account Number",self.accno)
        print("Name",self.personname)
        print("Balance is",self.balance)
        print("Bank name",self.bname)

obj=Bank(3354697523)
obj.setValues("arun",25)
obj.printValues()

obj.withdraw(74000)
obj.balaceEnquiry()
