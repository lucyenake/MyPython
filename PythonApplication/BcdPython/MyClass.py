from abc import ABCMeta, abstractmethod


#Abstract class and abstract method declaration
class Jungle(metaclass=ABCMeta):
    #def __init__(self):
    #    self.VisitorName="Stan"

    def __init__(self, name):
        self.VisitorName=name

    def WelcomeMessage(self):
        print ("Welcome to the jungle "+ self.VisitorName)

    # abstract method is compulsory to defined in child-class
    @abstractmethod
    def scarySound(self):
        pass


class RateJungle(Jungle):
    """ Some class info"""
    def __init__(self, name, feedback):       
        # feedback (1-10) : 1 is the best.
        self.feedback = feedback # Public Attribute
        # inheriting the constructor of the class
        super().__init__(name)
    
    #def __setattr__(self, feedback, value):
    #    if(feedback==34):
    #        pass

    # using parent class attribute i.e. visitorName
    def printRating(self):
        print("Thanks %s for your feedback" % self.visitorName)

    def scarySound(self):
        print("Print sound")

    def __del__(self):
        print("Del is here")

    def __str__(self):
        return("It is an object of class RateJungle")

    def __call__(self, aValue):
        print("object is used as function"+aValue)
        return "result"