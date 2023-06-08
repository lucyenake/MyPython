from ast import Num
from MyClass import Jungle, RateJungle, Spam
from MyRing import Ring
from Add import Add
import sys
import copy

print("Start")

#j= Jungle("Huhu");
#j.WelcomeMessage();

#y= Jungle("Vladut");
#y.WelcomeMessage();


def main():
    #j=Jungle('Vasile')
    #j.WelcomeMessage()

    r=RateJungle("gogu",56);
    r.WelcomeMessage()   
    r.scarySound()
    print(r)
    t=r("34")
    print(r.__doc__) # returns documentation from triple "
    print(r.__dict__)# returns atributes value
    x=3;
    print(id(x))
    print(type(x))
    y=34;
    print(x is y)
    y=x;
    print(x is y)

    x=[1,2,3]
    y=[2,3]
    if(type(x) is list):
        x.append(y)
    print(x)

    if isinstance(x,list):
        x.append(y)
    print(x)

    print(sys.getrefcount(x))

    a=[1,2,[10,20]]
    b=list(a)
    c=copy.deepcopy(a)
    print(a is b)
    a[0]=100
    a[2][0]=99;
    print(b)
    print(a)
    print(c)

    ty=str
    ty=int
    t=ty('10')
    print(type(t))

    x=(1,2,3,4,5,6,7)
    t=all(item>5 for item in x)
    print(t)

    t=any(item>4 for item in x)
    print(t)

    diff2Num=lambda x,y: x-y
    t=diff2Num(4,5)
    print(t)

    s = Spam()
    print(s.imethod())
    print(s.cmethod())
    print(s.smethod(56))

def MyMain():
    r=Ring("2017=08-10", "Gold", 5.5, 10.5, 10)
    print(r.metal)
    print(r.cost())
    print(r.area())

    r=Ring()
    print(r.metal)
    print(r.cost())
    print(r.area())
    print((r.area)())

    print (getattr(r,'metal'))
    setattr(r,'metal','GOLD')
    print (getattr(r,'metal'))

def WorkingWithAdd():    
    # method
    m = Add(x=4) # or m = Add(4)
    # for method, above x = 4, will be used for addition
    m.addMethod(10) # method : 14
    # classmethod
    c = Add(4)
    # for class method, class variable x = 9, will be used for addition
    c.addClass(10) # clasmethod : 19
    # for static method, x=20 (at the top of file), will be used for addition
    s = Add(4)
    s.addStatic(10) # staticmethod : 30
    #m.radius="jkj";
    m.radius(45)
    m.radius=90




if __name__=='__main__':
    main()
    MyMain()
    WorkingWithAdd()

