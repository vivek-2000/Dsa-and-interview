#ability to exist in multiple form
# A person at the same time can have different characteristic. Like a man at the same time is a father, 
# a husband, an employee. So the same person posses different behavior in different situations. This is called polymorphism.
#e.g max speed for different vechice so we can define 

#compile Time(Early Binding)

#It is also known as static polymorphism. This type of polymorphism 
#is achieved by Method overloading or operator overloading. But Java doesn’t support the Operator Overloading.

#Method Overloading -: same name but  different signture or no.of arugument

def add(datatype,*args):
    if datatype=="int":
        ans=0
    if datatype=="str":
        ans=""
    for i in args:
        ans+=i
    print(ans)
#overloading
add("int",5,7)
add("str","hi"," vivek"," tru")


#overriding(runtime)
#
#Whereas it is used in order to change the behavior of existing methods.

class BMW:
    def __init__(self,name):
        self.name=name
    def printname(self):
        print(self.name)
    def noofgear(self):
        print("4 gear")
class Audi(BMW):
    # Modified function that is
    # already exist in class BMW
    def noofgear(self):
        print("3 gear")
obj=Audi("audi")
obj.printname()
obj.noofgear()
