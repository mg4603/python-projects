class Parent():
    
    def implicit(self):
        print("PARENT implicit")

class Child(Parent):
    pass


if(__name__ == "__main__"):
    parent = Parent()
    child = Child()
    
    parent.implicit()
    child.implicit()