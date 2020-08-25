# parent   super   base

# child     sub     derived


class Parent:
    def phone(self):
        print("have oneplus 6T")


class Child(Parent):
    pass

p=Child()     #here p=obj we can use any letter

p.phone()