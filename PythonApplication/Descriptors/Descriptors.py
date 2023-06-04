class Decriptors:
    def __init__(self): #constructor       
        self.__bmi=0
    def __get__(self,instance, owner):
        return self.__bmi
    def __set__(self,instance, value):
        if isinstance(value,int):
            print(value)
        else: raise TypeError("Bmi can only be ineger")
        if value<0:
            raise ValueError("Bmi can never be less than zero") 
        self.__bmi=value
    def __delete__(self, isinstance):
        del self.__bmi   

class Person:
    bmi=Decriptors()
    def __init__(self, name, age, bmi): #constructor
        self.name=name
        self.age=age
        self.bmi=bmi       
    def __str__(self):
        return "{0} age  {1} with a bmi of {2}".format(self.name, self.age, self.bmi)

person1=Person("John",25,17)
print(person1)
person2=Person("Matei",25,47)
print("Last:")
print(person1)#atentie bmi is changed


