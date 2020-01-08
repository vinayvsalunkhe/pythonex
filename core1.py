#display data on the screen
"""
pyStr="python"
print(pyStr)
pychar="p"
print(pychar)
pyInt=100
print(pyInt)
PYFLOAT=10.25
print(PYFLOAT)
PyComplex=2+2j
print(PyComplex)
Pybool=True
print(Pybool)

#literal colection

pylist=[1,2,3,4,5]
print(pylist)

pytuple=(1,2,3,4,5)
print(pytuple)

pyset={1,2,3,4}
print(pyset)

pydict={1:"vinay", 2:"salunkhe"}
print(pydict)

#data types
a=10 # a is int object
print(type(a))
print(a)

a=10.5 # a is float object
print(type(a))
print(a)

d="python"
print(type(d))
print(d)

e=True
print(type(e))
print(e)

e=False
print(type(e))
print(e)

#special data type
f=None
print(type(f))
print(f)

#collections
d=[1,2,3]
print(type(d))
print(d)

d=(1,2,3)
print(type(d))
print(d)

d={1,2,3}
print(type(d))
print(d)

d={1:"python developer",2:"data scientist",3:"ml engineer"}
print(type(d))
print(d)


#swap variable
a=10
b=20
print(a,b)
a,b=b,a
print(a,b)

#del statement
a=10;b=20
print(a,b)
del a,b

#conversion
print(bin(23))
print(0b10111)
print(oct(23))
print(0o27)
print(hex(23))
print(0x17)



#write a program to read 2 nos. from the key board and print sum of them
X=input("ENTER FIRST NO.")
Y=input("ENTER SECOND NO.")
i=int(X)
j=int(Y)
print("the sum", i+j)

x=int(input("enter first no."))
y=int(input("enter second no."))
print("the sum:",x+y)

#read employee data from the keyboard and print that data
eno=int(input("enter employee no.:"))
ename=(input("enter employee name:"))
esal=float(input("enter employee salary:"))
eaddr=input("enter employee address:")
married=bool(input("employee married?[True|False]:",))
print("please confirm information")
print("employee no.:",eno)
print("employee name:",ename)
print("employee salary:",esal)
print("employee address:",eaddr)
print("employee married?:",married)
"""
"""#read multiple values from keyboard in single line
a,b=[int(x) for x in input("enter 2 numbers:").split()]
print("product is:",a*b)

#write a program to read 3 nos. from a keyboard seperated by ,
a,b,c=[float(x) for x in input("enter 3 float nos.:",).split(",")]
print("the sum is:",a+b+c)

#eval function
x=eval("10+20+30")
print(x)

x=eval(input("enter expression:",))
print(x)

#write a program to accept list from keyboard and display list
I=eval(input("enter list"))
print(type(I))
print(I)
"""

#math module
"""
#python number abs() function

print(abs(-1))
print(abs(127.5))
print(abs(-10))

#ceil()method
import math
print(math.ceil(-45.12))
print(math.ceil(100.17))
print(math.ceil(100.72))

#python no. floor() method
import math
print(math.floor(-45.17))
print(math.floor(100.12))
print(math.floor(100.72))

#math fabs()
import math
print(math.fabs(1))
print(math.fabs(10))
print(math.fabs(-100))

#math factorial()
import math
print(math.factorial(3))
print(math.factorial(6))
print(math.factorial(2))

#math. fsum(iterable)
import math
print(math.fsum((1,2,3,4)))
print(math.fsum([1,2,3]))
print(math.fsum({1.3,1.2,2.2}))
pyset={1,2}
print(math.fsum(pyset))

#math.pow(x,y)
import math
print(math.pow(2,2))
print(math.pow(3.2,2))
print(math.pow(2,3))
print(math.pow(3,3))

#python no. round() function
print(round(125.99))
print(round(125.99,2))
print(round(125.599,3))

#python sqrt() method
import math
print(math.sqrt(4))
print(math.sqrt(5))
print(math.sqrt(6))

#working with random nos. in python
import random
print(random.random())
print(random.random())

#generating random int between x & y
import random
print(random.randint(1,10))
print(random.randint(1,100))
print(random.randint(1,13))
print(random.randint(10,27))

#generating random range between(x,y)
import random
print(random.randrange(1,10))
print(random.randrange(10,57))

#generating random floats between (x,y)
import random
print(random.uniform(1,2))
print(random.uniform(10,15))


#picking a random elements from a list
import random
print(random.choice([1,2,3,4]))
pylist=[4,5,7,9,10]

print(random.choice(pylist))

#list data structures concatenation
pylist1=[1,2,3,4]
pylist2=[10,11,12,13]
pylist=pylist1+pylist2
print(pylist1*2)
print(pylist2*2)
print(pylist)

#tuple datastructure concatenation
pytuple1=(1,2,3,4)
pytuple2=(10,11,12,13)
pytuple=pytuple1+pytuple2
print(pytuple1*2)
print(pytuple*2)
print(pytuple)
"""

#list data structures concatenation
pylist1=[1,2,3,4]
pylist2=[10,11,12,13]
pylist=pylist1+pylist2
print(pylist1*2)
print(pylist2*2)
print(pylist)

print(len(pylist))
print(len (pylist1))
print(len(pylist2))
print(1 in pylist2)
print(1 in pylist1)
print (x in pylist):
    print(x,end=" ")

































