# a=input("Enter name: ")
# b=int(input("Employee no.: "))

# class Calculate:
# 		def add_num(self,a,b):
# 			return a+b

# calculate = Calculate()	
# print(calculate.add_num(a,b))

class Student:
	
	def __init__(self):
		self.o_name="MIT"
		self.d_name="BIO"
	def set_student_name(self,name):
			self.s_name=name 
class English(Student):
	def set_english(self,marks):
		self.s1_marks=marks 
class Maths(Student):
	def set_maths(self,marks):
		self.s2_marks=marks
class AverageMarks(	English	, Maths):
	
	def display(self):
		print("Information about the Student")

		print(f"Student Name: {self.s_name} \nOrganisation: {self.o_name} \nDepartment: {self.d_name} \nAverage Marks {(self.s1_marks+self.s2_marks)/2}")
		


a=input("Enter name: ")
b=int(input("Marks for English: "))
c=int(input("Marks for Maths: "))
d=AverageMarks()
d.set_student_name(a)
d.set_english(b)
d.set_maths(c)
d.display()
