#!/usr/bin/env python3

class Parent():
    
    def override(self):
        print("PARENT override()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")

if(__name__ == "__main__"):
    parent = Parent()
    child = Child()

    parent.override()
    child.override()