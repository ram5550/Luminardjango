class Parent:
    def m1(self):
        print("inside parent1")


class Child:
    def m1(self):
        print("inside child")

class SubChild(Parent,Child):
    def m3(self):
        print("inside subchild")


s=SubChild()
s.m3()
s.m1()

