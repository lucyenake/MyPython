def myfunction(a):
    return a*2;

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
