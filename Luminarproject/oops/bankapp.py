import datetime
class Bank:
    bname="SBK" #static variable-->accesed by className.variablename
    def __init__(self,accno,personname):
        self.accno=accno
        self.personname=personname
        self.balance=3000


    def withdraw(self,amount):

        if(amount>self.balance):
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print("Your",Bank.bname,"has been debited with",amount,"on",datetime.date.today())

    def deposit(self,amount):
        self.balance+=amount
        print("Your",Bank.bname,"has been credited with",amount,"on",datetime.date.today())

    def balaceEnquiry(self):
        print("Account Number",self.accno)
        print("Name",self.personname)
        print("Balance is",self.balance)
        print("Bank name",self.bname)

obj=Bank(3354697523,"arun")


obj.withdraw(5000)
obj.balaceEnquiry()
