def myfunction(a):
    return a*2;

# List Comprehension
num=[1,2,3,4,5,6,7]
squares=[]

for n in num:
    squares.append(n**2)

print(squares)

squares=[n**2 for n in num] #comprehension
print(squares)

listt=[1,2,3,4,5]
list1=[2,3,4,5,6]

intersection=[]
for x in listt:
    for y in list1:
        if x==y:
            intersection.append(x)
print (intersection)

intersection=[x for x in listt for y in list1 if x==y] #comprehension
print(intersection)

x=[[a**2, a**3] for a in listt]
print(x)

x=list(map(lambda x:x, "Hello"))  #lambda
print(x)

op=open("Python.txt", "r")
output=[i for i in op if "2" in i]
print(output)

print(myfunction(3))

y=[myfunction(a) for a in range(10)]
print(y);

# Dictionary Comprehension
mydict={'a':1, 'b':2, 'c':3, 'd':4}

print(mydict)
x= mydict.keys()
print(x)
x= mydict.values()
print(x)

x= mydict.items()
print(x)

new_dict={k:v*2 for (k,v) in mydict.items()}
print(new_dict)

new_dict={k*2:v for (k,v) in mydict.items()}
print(new_dict)

mydict={j:j**2 for j in range(10) if j%2==0}
print(mydict)

feh={'temp1':10,'temp2':20,'temp3':30,'temp4':40,'temp5':50}
cel=list(map(lambda x: (float(5)/9)*(x-32),feh.values()))
cel_dic=dict(zip(feh.keys(),cel))

print(cel_dic)

#Set Comprehension

input=[1,2,2,2,3,3,3,3,4,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,8,8,8,8]
output=set()
for var in input:
    if var%2==0:
        output.add(var)
print (output)

output={var for var in input if var%2==0}
print(output)

#Generator Comprehension
input =[1,2,3,4,4,4,5,6,7,7,7,7]

output=(var for var in input if var%2==0)
for var in output:
    print(var, end='')
