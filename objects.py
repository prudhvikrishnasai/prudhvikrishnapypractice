"""class computer:
    def config(self):
        print("i5,16gb,cpu")

com1=computer()        #defining objects using constructors
com2=computer()

computer.config(com1)      #calling methods
computer.config(com2)

com1.config()               #callng methods
com2.config()"""

"""class computer:
    def __init__(self,cpu,ram):         #__init__ method is called automatically 
        self.var1=cpu                    # self refers to objects and assigning variables to tht object
        self.var2=ram
    def config(self):                   # we gave only one argument for config but we r using cpu and ram arguments from init method
        x=5
        print(x)
        print("config is"+self.var1,self.var2)
    def configs(self,a):
        print("config is"+str(a))

com1=computer(" i5","16gb")
com2=computer(" i3","8gb")

com1.config()
com1.configs(5)
com2.config()"""

"""class computer:
    def __init__(self):
        self.name="Prudhvi"                 
        self.age=23                         
    def person(self):
        self.age=34
        print(self.age)
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=computer()
c2=computer()
c1.person()
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
print(c1.age)
print(c2.age)"""

"""class car:
    wheel=4                     #if we define a variable inside class n outside init it becomes class varialbe/static variables it affects the whole class
    def __init__(self):
        self.mil=10             #if we define a variable inside init it becomes instance variable it affects only perticular obj tht we r performing change on
        self.com="bmw"
c1=car()
c2=car()
c1.mil=20
car.wheel=5
print(c1.mil,c1.com,car.wheel)
print(c2.mil,c2.com,car.wheel)"""
                                #TYPES OF METHODS
"""class student:
    school="Krishacadamy"
    def __init__(self,m1,m2,m3):      #instance method
        self.m1=m1
        self.m2=m2              #getting inputs from constructor
        self.m3=m3
    def get_m(self):            #getter instance method
        return self.m1
    def set_m(self,value):      #setter instance method
        self.m1=value
    def avg(self):              #instance method
        return (self.m1+self.m2+self.m3)/3
    @classmethod                #decorator to be used while using class method
    def info(cls):              #put cls as argument for class methods
        return cls.school
    def amst(self):             #amstrong number till 1000
        x = []
        for i in range(1000):

            y=i%10
            z=(i//10)%10
            e=1//100
            if y**3+z**3+e**3 ==i:
                x.append(i)
        print(x)

s1=student(20,45,67)
s2=student(36,78,43)
print(s1.m1)
print(s1.get_m())
print(s1.info())
print(s1.avg())
s1.amst()"""

"""class student:                      #outer class
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.lap=self.laptop()              #assigning laptop class to lap
    def show(self):
        print(self.name,self.age)
        s1.lap.show()
    class laptop:                           #inner class
        def __init__(self):
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.cpu,self.ram)
s1=student("prudhvi",23)
s2=student("jsj",32)
s1.show()
print(s1.lap.ram)
s3=student.laptop()
s3.show()"""
                            #INHERITENCE
"""class A:
    def __init__(self):
        print("in A init")
    def show1(self):
        print("Showing 1")
    def show2(self):
        print("Showing 2")
class B(A):                     #single level inheritance
    def __init__(self):
        super().__init__()          #for accessing init function of super class A
        print("in B init")
    def show3(self):
        print("Showing 3")
    def show4(self):
        print("Showing 4")
class C(B):                     #Multi level inheritance
    def show5(self):
        print("Showing 5")
    def show6(self):
        print("Showing 6")
class D:
    def __init__(self):
        print("in D init")
    def show5(self):
        print("Showing 5")
    def show6(self):
        print("Showing 6")
class E(D,A):                   #Multiple inheritance #while accessing the init function it follows MRO(method resolution order) which means it starts from left. in this case D
    def show7(self):
        super().show6()         #calling method from super class using super method
        print("Showing 7")
    def show8(self):
        print("Showing 8")
s1=B()
s1.show1()
s2=E()
s2.show5()
s2.show7()"""
                        #POLYMORPHISM
"""class laptop:
    def perform(self,ide):
        ide.execute()                               #Duck Typing
class pycharm:
    def execute(self):
        print("Execution")
        print("Compiling")
class netbeans:
    def execute(self):
        print("Running")
        print("Testing")

ide=netbeans()
s1=laptop()
s1.perform(ide)
print(type(ide))"""

"""class student:                          #operator overloading
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

s1=student(24,67)
s2=student(32,65)
s5=student(30,65)
s3=s1+s2            # + means in backend __add__ happens normally
s4=s1.m1+s5.m1
print(s4)
print(s3.m1)
if s1>s5:               # > means in backend __gt__ happens normally
    print("s1 wins")
else:
    print("s2 wins")


print(type(s1))"""

#method overloading- if two methods in a class have same name but different parameters. generally in python we dont have this but we can have this using some  trick check it in navin reddy videos
#method overriding - if parent class n child class has methods with same name.

"""class sum:
    def add(self,a=None,b=None,c=None):         
        if a!=None and b!=None and c!=None:
            d=a+b+c
            print(d)                            #Method overloading using this trick
        elif a!=None and b!=None:
            d = a + b
            print(d)
        else:
            print(a)
s1=sum()
s1.add(3,4)"""







"""class A:
    def show(self):
        print("I have phn")
class B(A):                     #Method overridding shw method in A is overriden by show method in B
    def show(self):
        print("I have no phn")
s1=B()
s1.show()"""

                                #TYPES OF ERROES
"""Compile Time Error: Compile Time Errors are those errors which prevent the code from running because of an incorrect syntax 
such as a missing semicolon at the end of a statement or a missing bracket, class not found, etc. ... 
Compile Time Errors are sometimes also referred to as Syntax errors"""

"""A logic error (or logical error) is a mistake in a program's source code that results in incorrect or unexpected behavior. ...
For example, assigning a value to the wrong variable may cause a series of unexpected program errors. 
Multiplying two numbers instead of adding them together may also produce unwanted results."""

"""A runtime error is a program error that occurs while the program is running. ...
Crashes can be caused by memory leaks or other programming errors.
Common examples include dividing by zero, referencing missing files,calling invalid functions, or not handling certain input correctly."""

"""a=10
b=0

try:                                        #tries if it works
    print("resource open")                  #if u what to open any file
    c=a/b
    print(c)
    k=int(input("Enter a number:"))
    print(k)
except ZeroDivisionError as e:              #whn u know it would be zero error
    print("Hey, b cannot by 0.",e)
    b = int(input("Enter other number for b:"))
    c=a/b
    print(c)
except ValueError as e:                     #whn u know it would be input value error
    print("Hey don't enter a string.",e)
except Exception as e:                      #whn u dont know what kind of error it might be
    print("Something went wrong.",e)
finally:                                    #it runs irrespective of exceptions(runs no matter what
    print("resource closed")                #if u open a file u should close it"""

#Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
#executing multiple methods of multiple classes at a time. like we do multi tasking
"""from time import sleep
from threading import *
class hello(Thread):        #extending thread class
    def run(self):          #run method should be used
        for i in range(5):
            print("Hello")
            sleep(1)        #sleep() is used to provide time gap between nxt iteration
class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1=hello()
t2=hi()
t1.start()                      #start() should be called in threads .instead of calling by method name
sleep(0.2)                      #allowing both threads to have their time gap so tht they dont colide
t2.start()
t1.join()                       #join() is used to let t1 n t2 threads to complete first n then exceute bye
t2.join()
print("Bye")"""

                                #FILE HANDLING
"""f=open('myfile','r')            #use open method and use file name with extension if any to get the file.use r for reading a file
print(f.readline())             #for reading one line from the file
print(f.read())                 #for reading everything from file

f1=open('abc','w')              #use file to create the fle n use w to write. it juz rights but dont append
f1.write("something")

f2=open('abc','a')              #use file to create the fle n use a to append.
f2.write("jkfkf")"""

"""f=open('myfile','r')
f1=open('abc','w')
for i in f:                 #for getting all the data from myfile to abc
    f1.write(i)"""

# to access a globle variable inside a function put global()['variable name']

