from stat import FILE_ATTRIBUTE_ARCHIVE, FILE_ATTRIBUTE_INTEGRITY_STREAM


x=56
class Add(object):
    x = 9 # class variable
    
    def __init__(self, x):
        self.x = x # instance variable
        self.radius=89;
    
    def addMethod(self, y):
        print("method:", self.x + y)

    @property
    # method-name should be same as attribute i.e. 'radius' here
    def radius(self):
        return self._radius # _radius can be changed with other name

    @radius.setter
    def radius(self, val):
    # 'val' should be float or int
        if not isinstance(val, (float, int)):
            raise TypeError("Expected: float or int")
        self._radius = float(val)

    # Multiple constructor
    @classmethod
    # as convention, cls must be used for classmethod, instead of self
    def addClass(self, y):
        print("classmethod:", self.x + y)
    
    @staticmethod
    def addStatic(y):
        print("staticmethod:", x + y)




