#!/usr/bin/env python3

class Parent():
    
    def override(self):
        print("PARENT override()")

class Child(Parent):
    
    def override(self):
        print("CHILD override")
        