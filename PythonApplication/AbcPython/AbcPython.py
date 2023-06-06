from math import sin
import matplotlib.pyplot as plt
from MyFunctions import MyAverage
from MyFunctions import MyStat
from MyClasses import MyCar
#from math import sin , cos
#from math import *

#import math
#x = 3.14
#y = math.sin ( x )
#print ( y )

#import math as mt
#x = 3.14
#y = mt.sin ( x )
#print ( y )


x=1 #int
y=2.3 #float
z=3+3j #complex

print(z)

mystr="Hello"
mystr='Hello'
print(mystr)

a = "He l l o World ! "

print (a)
print (a [ 1 ])
print (a[ 2 : 5])
print (len ( a ) )
print (a.lower ( ) )
print (a.upper ( ) )
print (a.replace ( "H" , "J" ) )
print (a.split ( " " ) )

print ( "Enter your name : " )
#x = input ( )
#print ( "Hel lo , " + x )

x = 3.14
y = sin ( x )
print ( y )

x = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]

y = [ 5 , 2 ,4 , 4 , 8 , 7 , 4 , 8 , 10 , 9 ]

plt.plot (x , y )
plt.xlabel ( 'Time ( s ) ' )
plt.ylabel ( ' Temperature ( degC) ' )
plt.show()

if 4<5:
    print("ok")
else:
    print("Nok")

data = [1.6, 3.4, 5.5, 9.4 ] #array
N = len (data)
print (N)
print (data[2])
data [2] = 7.3
print (data[2])
for x in data :
    print (x)
data.append (11.4)
N = len (data)
print (N)
for x in data :
    print(x)

for x in range (N):
    print (x)

def myfunction(x):
    print('This is my function'+x)

myfunction("Lenache")

print(MyAverage(89,98))

data=[1,5,6,7,8,9]
totalsum, mean=MyStat(data)
print ('Total sum is:' + str(totalsum)+' , mean is:'+str(mean))

class Car:
    model="Volvo"
    color="Blue"

car=Car()
print(car.model)
print(car.color)

car1=Car()
car1.model="Audi"
car1.color="White"

print(car1.model)
print(car1.color)

print(car.model)
print(car.color)

myCar1=MyCar('Skoda','white')
print(myCar1.model)
myCar1.displayCar()

f = open ( "myfile.txt " , "+a")
data = "Helo World"
f.write (data)
f.close()

f = open ( "myfile.txt " , "r")
data=f.read()
print(data)
f.close()

print('{:06b}'.format(11)) # decimal to binary conversion with 6 places
print('{:6b}'.format(10))
print('{:06x}'.format(10)) # decimal to hex conversion with 6 places
print('{:03x}'.format(0b1111)) # binary to hexadecimal with 3 places

print("{:b}".format(10).zfill(15)) # number = 10, total places = 15
print("{:x}".format(10).zfill(15)) # number = x, total places = 15
print("{:o}".format(10).zfill(15)) # number = x, total places = 15
print("{:d}".format(x).zfill(0b11)) # number = x, total places = 3
print("{:d}".format(x).zfill(0o11)) # number = x, total places = 9

arr = [10, 20, 30]

for i in range(len(arr)): # bad practice
    print(2*arr[i]) # 20, 40, 60

for i in arr: # good practices
    print(2*i) # 20, 40, 60

for i in reversed(arr): # print in reverse order
    print(2*i) # 60, 40, 20

for i, a in enumerate(arr):
    print(i, ':', 2*a)

x = [1, 2, 3]
a, b, c = x #Unpacking

print(a)
print(b)
print(c)

student = ["Tom", 90, 95, 98, 30]
Name, *Marks, Age = student
print(Marks)

x = 3
y = 2
z = 5
x, y, z = y, z, x








