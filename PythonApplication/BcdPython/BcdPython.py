from MyClass import Jungle, RateJungle

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

if __name__=='__main__':
    main()

