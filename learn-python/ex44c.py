class Parent():
    
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


if(__name__ == "__main__"):
    parent = Parent()
    child = Child()

    parent.altered()
    child.altered()