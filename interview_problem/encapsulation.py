#Encapsulation is the process of binding data member and method of program together to do specific job without revealing 
#unncessory details
# e.g sales and finiancial department



class Sales:
    def __init__(self) -> None:
        self.name="vivek"
        self.__maxprice=100
    def accessmax(self):
        return self.__maxprice
obj=Sales()
#not able to direct access
#print(obj.__maxprice)
print(obj.accessmax())




