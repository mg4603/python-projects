class Other():
    
    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")

class Child():

    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()

    