
class Person:

    #method
    def __init__(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender
    def printValues(self):
        print(self.age)
        print(self.name)
        print(self.gender)

obj=Person(27,"rahul","male")

obj.printValues()
