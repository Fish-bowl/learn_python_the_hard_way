
class Animal(object):
    pass

#dog is a animal that has a name
class Dog(Animal):

  def __init__(self, name):

    self.name = name

#cat is a animal
class Cat(Animal):

  def __init__(self, name):
    #that has a name 
    self.name = name 

#person is a object 
class Person(object):

  def __init__(self, name):
    #that has a name 
    self.name = name 

    #person has no pet  
    self.pet = None

  #employee is a person 
class Employee(Person):

  def __init__(self, name, salary):
    #bind employee self to name?
    super(Employee, self).__init__(name)
    # employee has a salary
    self.salary = salary

#fish is an object 
class Fish(object):
    pass 

#Salmon is a fish 
class Salmon(Fish):
    pass 

#halibut is a fish 
class Halibut(Fish):
    pass 


#rover is a dog 
rover = Dog("Rover")

#satan is a cat 
satan = Cat("Satan")

#mary is a person 
mary = Person("Mary")

#mary has a pet 
mary.pet = satan 

#frank is an emploeyy
frank = Employee("Frank", 120000)

#frank has a pet 
frank.pet = rover 

#fipper is a fish 
flipper = Fish() 

#crouse is a salmon 
crouse = Salmon()

#harry is a halibut 
harry = Halibut()
