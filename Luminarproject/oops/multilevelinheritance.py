class Parent:
    def m1(self):
        print("inside parent1")


class Child(Parent):
    def m2(self):
        print("inside child")

class SubChild(Child):
    def m3(self):
        print("inside subchild")

#subchild
su=SubChild()
su.m1()
su.m2()
su.m3()


#child
ch=Child()
ch.m1()
ch.m2()
#ch.m3() #error because child will not inherit subchild