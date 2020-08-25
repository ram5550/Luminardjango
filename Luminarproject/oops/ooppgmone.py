#object oriented programming

#1)class
#2)object
#3)reference

#1)class ?-> plan,design,blue print,template

#2)object ->real world entity

#3)reference-> Tv(class)->mitv<-remote(reference)




# class ClassName:


class Person:

    #method
    def setValues(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender
    def printValues(self):
        print(self.age)
        print(self.name)
        print(self.gender)

obj=Person()

obj.setValues(27,"rahul","male")
obj.printValues()
