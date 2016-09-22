"""
Author : Nano Y
Date   : 20-09-2016

Simple demo of a scatter plot.
https://www.tutorialspoint.com/python/python_classes_objects.htm
http://radek.io/2011/07/21/private-protected-and-public-in-python/
http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html
http://stackoverflow.com/questions/6434482/python-function-overloading
https://www.tutorialspoint.com/python/python_modules.htm
"""
import numpy as np
import matplotlib.pyplot 


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

matplotlib.pyplot.scatter(x, y, s=area, c=colors, alpha=0.5)
matplotlib.pyplot.show()
	
class Employee:
   'Common base class for all employees'
   empCount = 0
   __secretCount = 0
   
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      #Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
	  
   def addSalary(self,intAddSalary):
		self.salary = self.salary + intAddSalary  
		
   def __privateMethod(self) :
		print "This is Private Method, Only accessible inside this class, cant be derived to a child class"
	
   def _protectedMethod(self) :
		print "This is Protected Method, can be accessed inside this class,child class"
		
   def publicMethod(self) : 
		print "This is public Method, can be accessed inside this class, child class, and instance of this class"

#INHERITANCE	
class Manager(Employee):
	def __init__(self, name, salary, tunjangan):
		self.name = name
		self.salary = salary
		self.tunjangan = tunjangan
		print "Object of Manager created"
		self._protectedMethod()
		self.publicMethod()
		self._Employee__privateMethod() # SEHARUSNYA TIDAK BISA DIAKSES DI CLASS TURUNAN
		
	def addSalary(self): # overriding method
		self.salary = self.salary + ( 0.2 *  self.salary)	
		
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

print "Check empCount class variables : "
print emp1.empCount
emp1.empCount = 11 #INSTANCE VARIABEL DARI EMP1
print emp1.empCount
emp2.empCount = 22
print emp2.empCount  # INSTANCE VARIABEL DARI EMP2
print Employee.empCount #CLASS VARIABLE


print emp1.name
print emp2.name
#print Employee.name

emp1.addSalary(500)
emp2.addSalary(5000)

print "emp1 new salary :", emp1.salary
print "emp2 new salary :", emp2.salary

#http://pythoncentral.io/pythons-range-function-explained/ Function Overloading
for i in range(5):
	print(i)
	
for i in range(3, 6):
	print(i)
	
for i in range(4, 10, 2):
	print(i)

#Cek Private,protected,Public ACCESS MODIFIER ANEH DI PYTHON ??? 
emp1.publicMethod()
emp1._protectedMethod() # SEHARUSNYA TIDAK BISA DIAKSES DARI OBJECT
emp1._Employee__privateMethod() #SEHARUSNYA TIDAK BISA DIAKSES DARI OBJECT

print "Create Object of Manager : see the constructor "
jokowi = Manager("Jokowi",10000,5000)
jokowi._protectedMethod()
jokowi.addSalary() 

#jokowi.__privateMethod() #ERROR GIVEN NORMAL CONDITION SESUAI ATURAN ... BUT ,...
jokowi._Employee__privateMethod() #WORST!! SEHARUSNYA TIDAK BISA DIAKSES DARI CHILD OBJECT
print "Tunjangan Manager Jokowi :", jokowi.tunjangan
print "Salary Manager Jokowi:", jokowi.salary
#jokowi.addSalary(5000)  #ERROR GIVEN coz 

