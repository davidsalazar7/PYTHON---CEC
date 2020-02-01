# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:34:54 2020

@author: CEC
"""
'''
class Employee:
    'Common base class for all empleyees'
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
        
    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)
        
    def displayEmployee(self):
        print('Name: ',self.name,', Salary: ',self.salary)
        
'This would create first object of Employee class'
emp1=Employee('Zara',2000)
'This would create second object of Employee class'
emp2=Employee('Manni',5000)
emp3=Employee('Man',4000)
emp4=Employee('David',1000)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
'''

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)