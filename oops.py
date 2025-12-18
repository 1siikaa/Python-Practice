class empty:
    pass

obj1 = empty()
print(obj1)

#############################

class filled:
    x = 5

obj2 = filled()
obj3 = filled()
print(obj2.x)
del obj2
#print(obj2.x) # obj2 is deleted now. It will give attribute error.
print(obj3.x)

#############################
# python __init()__ method

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

obj4 = Person("Vanshika", 24)
print(obj4.name)
print(obj4.age)        

##############################
# self method

class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student1(self):
      #self.name = "Vanshika"
      return f"Hello, my name is {self.name}"

obj5 = Students("Vanshika2.0", 24)
print(obj5.student1())

#####################################
# call one method from another using self

class Person:
    def __init__(self, name):
        lastName = ""
        self.name = name

    def greet(self):
        return f"Hello, {self.name}" 

    def welcome(self):
        message = self.greet()
        return f"{message}! Welcome to our website."

obj6 = Person("Vanshika3.0")
print(obj6.welcome())
del obj6.name
Person.lastName = "Dubey"
print(obj6.lastName)
# print(obj6.welcome())  -> attribute error Person object has no attribute name
# add new property to existing object
obj6.name = "Vanshika"
obj6.age = 24
obj6.city = "Ghaziabad"
print(f"name: {obj6.name} | age: {obj6.age} | city: {obj6.city}")

###############################
# __str___() method
# The __str__() method controls what is returned when the object is printed
class Person:
   def __init__(self, firstName, lastName):
     self.firstName = firstName
     self.lastName = lastName

   def __str__(self):
     return f"My name is {self.firstName} {self.lastName}"

   def firstFunction(self):
    return f"My name is {self.firstName} {self.lastName}. I am so good."

obj7 = Person("Vanshika", "Dubey")
print(obj7)       

################################
#Inheritance and overriding

class Student(Person):
    def __init__(self, firstName, lastName, year):
        super().__init__(firstName, lastName)
        self.graduationYear = year

    def __str__(self):
        return f"I am {self.firstName} {self.lastName}. I graduated in {self.graduationYear}"

    def secondFunction(self):
         return f"I am {self.firstName} {self.lastName}"   

obj8 = Student("Addu", "Dwivedi", 2021)
print(obj8)

