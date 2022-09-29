# Animal is-an object
class Animal:
    pass

## Dog is-an Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-an Animal
class Cat(Animal):

    def __inti__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-an object
class Person():

    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a Pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-an object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a Pet which is-a Cat which has-a name Satan
mary.pet = satan

## frank is-an Employee with name Frank and has-a salary of 120000
frank = Employee("Frank")

## frank has-a Pet which is-a Dog which has-a name Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()