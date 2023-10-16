
from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass
class Rectangle(Shape):
	def area(self,length,breadth):
		return length*breadth	
class Circle(Shape):
	def area(self,radius):
		return (3.14*radius*radius)
r=Rectangle()	
c=Circle()

l=int(input("Length of Rectangle: "))
b=int(input("Breadth of Rectangle: "))

radius=int(input("Radius of Circle: "))

print(f"Area of Rectangle: {r.area(l,b)} \nArea of Circle: {c.area(radius)} ")