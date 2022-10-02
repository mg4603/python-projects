class Parent():
    
    def override(self):
        print("PARENT override()")
    
    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print("PARENT altered()")


class Child():
    
    def override(self):
        print("CHILD override")
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


if(__name__ == "__main__"):
    parent = Parent()
    child = Child()

    parent.implicit()
    child.implicit()

    parent.altered()
    child.altered()

    parent.override()
    child.override()