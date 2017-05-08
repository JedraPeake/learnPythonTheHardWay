## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## dog is an Animal
class Dog(Animal):

    def __init__(self, name):
        ## a dog has a name
        self.name = name

## cat is an Animal
class Cat(Animal):

    def __init__(self, name):
        ## a cat has a name
        self.name = name

## a preson is an object
class Person(object):

    def __init__(self, name):
        ## a person has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## an employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## an empployee has a salary
        self.salary = salary

## a fish is an object
class Fish(object):
    pass

## a salmon is a Fish
class Salmon(Fish):
    pass

## a halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has a pet called satan
mary.pet = satan

## frank is an Employee, that has a salary of 1200000
frank = Employee("Frank", 120000)

## frank has a pet called rover
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## coruse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
