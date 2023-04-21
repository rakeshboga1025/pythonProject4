import sys

def function():
    pass

print(type(1)) #<class 'int'>
print(type("")) # <class 'str'>
print(type([]))  # <class 'str'>
print(type({})) # <class 'dict'>
print(type(()))  #<class 'tuple'>

print(type(object))  # <class 'type'>
print(type(function())) # <class 'NoneType'>
print(type(sys))  #<class 'module'>


class Person:
    def __int__(self, name, age):
        self.name = name
        self.age =age

P1 = person("Rakesh", 28)
print(P1.name)
print(P1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
   self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
