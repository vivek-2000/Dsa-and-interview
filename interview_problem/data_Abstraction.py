#providing//Allow  only essential information about the data to the outside world, hiding the background details or implementation.
#e.g otp generating mechanism  
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofside(self):
        pass
#inheritance
class Triangle(Polygon):
    #overriding
    def noofside(self):
        print("I have 3 side")
t=Triangle()
t.noofside()
#we cannot define object abstract class


