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