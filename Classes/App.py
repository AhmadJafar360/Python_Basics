# Classes
class Point:
    def move(self):
        print("move")
    
    def  draw(self):
        print("draw")

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

# Contructors
class Client:
    def __init__(self, x, y):
      self.x = x
      self.y = y
    
    def love(self):
        print("love")
    
    def story(self):
        print("story")

point = Client(10, 20)
point.x = 30
print(point.x)

# Solution Question
class Person:
    def __init__(self, name):
      self.name = name
    
    def talk (self):
        print(f'Hallo, Saya {self.name}')

jafar = Person("Jafar Ali")
jafar.talk()

# Inherite
class mammal:
    def walk(slef):
        print("walk")
    
class Dog(mammal):
        pass

class cat(mammal):
        pass

dog1 = Dog()
dog1.walk()