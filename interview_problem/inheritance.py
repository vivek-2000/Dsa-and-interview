#Inheritance is the capability of one class to derive or inherit the properties from another class.
class Person:
    def __init__(self,name) -> None:
        self.name=name
    def printname(self):
        print(self.name)
    def isstudent(self):
        print("Yes !")
#inhert
class Student(Person):
    def isstudent(self):
        print("NO !")
obj1=Person("Anshu")
obj1.printname()
obj1.isstudent()
#inherhit parent one
obj2=Student("Vivek")
obj2.printname()
obj2.isstudent()