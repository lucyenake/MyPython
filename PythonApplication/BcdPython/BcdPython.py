from ast import Num
from MyClass import Jungle, RateJungle, Spam
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


if __name__=='__main__':
    main()

