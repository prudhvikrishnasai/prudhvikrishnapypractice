from array import*
from numpy import *
"""num=int(input("Number"))
for i in range(2,num):
    print(i)
    if num%i==0:                                #Prime Numbers
        print("Not Prime"+str(i))
        break
else:
    print("Prime")
x=2
y=2
z=x%y
print(z)"""

"""from array import*      #importing all the methods, functions,everything from the array module
vals= array('i',[5,6,7,8,9])
newArry= array(vals.typecode,(a*a for a in vals))   #working with arrays
'''for e in range(len(newArry)):
    print(newArry[e])'''
for e in newArry:
    print(e)"""

'''import array as arr  #juz importing the array module
k=arr.array('i',[6,7,8])                               #feel the importing difference
print(k)'''
"""arr=array('i',[])
le=int(input("enter length of the array"))
for i in range(le):
    x=int(input("enter value"))
    arr.append(x)
print(arr)

k=0
val=int(input("enter value to search the index of it"))
for e in arr:
    if e==val:
        print(k)                               #finding the index of an element manually
        break
    k+=1
print(arr.index(val))"""                            #finding the index of an element with method

"""def add_sub(x,y):
    c=x+y
    d=x-y                                           #returning values in functions
    return c,d
result1,result2= add_sub(5,4)
print(result1,result2)"""

"""def person(name,age,marks):
#def person(name,age=18):               arguments in function
    print(name)
    print(age)
    print(marks)
person('krish',marks=25,age=18)"""

"""def add(a,*b):
    c=0
    for i in b:                 #*b is a tuple that holds multiple values without keyword
        c+=i
    print(c)
add(3,4,5,6)"""

"""def person(name,**data):
    print(name)                 #**data 2 stars are used for holding multiple data using keywords
    print(data)
person('krish',age=23,city='Tirupati',mob='8394783')"""

"""def person(name,**data):
    print(name)                 #**data 2 stars are used for holding multiple data using keywords
    for i,j in data.items():
        print(i,j)
person('krish',age=23,city='Tirupati',mob='8394783')"""

"""a=10
b=3
def local_global():
    a=15
    x=globals()['a']
                                        #local n global variables
    print(a)
    print(id(a))

    print(x)
    print(id(x))
local_global()
print(a)
print(id(a))"""

"""def lists(lst):
    ev=0
    even=[]
    od=0
    odd=[]
    for i in lst:
        if i%2==0:
            even.append(i)
            ev+=1
        else:
            odd.append(i)
            od+=1
    return ev,even,od,odd

lst=[2,45,3,6,87,9,67,47]
ev,even,od,odd=lists(lst)
print("there are {} even and they are {}. there are {} odd and they are {}".format(ev,even,od,odd))"""

"""n=int(input("enter number"))
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a ,end="\t")
        print(b ,end="\t")                #fibbinacci
        for i in range(2,n):
            c=a+b
            print(c, end="\t")
            a=b
            b=c
fib(n)"""

"""n=int(input("enter number"))

def fac(n):
    x = 1
    for i in range(1,n+1):
        x=x*i
    print(x)
fac(n)"""
"""n=int(input("enter number"))
def re_fac(n):
    if n==0:
        return 1                #factorial with recussion
    return n*re_fac(n-1)
res=re_fac(n)
print(res)"""
"""f=lambda a,b:a*b
res=f(5,6)
print(res)"""

"""from functools import reduce
num=[4,5,67,87,4,56]
evens=list(filter(lambda n:n%2==0,num))                         #filter,map,reduce
double=list(map(lambda n:n*2,filter(lambda n:n%2==0,num)))
sum=reduce(lambda a,b:a+b,double)
print(evens)
print(double)
print(sum)"""

"""def div(a,b):
    print(a/b)
def smart_div(func):            # here it is taking function as a parameter
    def inner(a,b):
        if a<b:
            a,b=b,a                     #decorators are used to modify existing function without touching it
            return func(a,b)
    return inner

div1=smart_div(div)
div1(2,4)"""


"""def amst():                                 # amstrong number
    x = []
    for i in range(1000):

        y = i % 10
        z = i // 10
        w = z % 10
        e = z // 10
        if y ** 3 + w ** 3 + e ** 3 == i:
            x.append(i)
    print(x)
amst()"""
"""# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")"""

"""def unpack(p,w,e,r):
    print(p+r)
a=[2,3,4,5]                     #important
unpack(*a)"""

"""list=[2,3,4,5,6]
num=int(input("search for:"))           #linear search
for i in range(len(list)):
    if num==list[i]:
        print("found {0} in".format(list[i])+ str(i))
        break
else:
    print("Not found")"""

"""class linear:
    def __init__(self,list,n):              #linear search using classes
        self.list=list
        self.n=n

    def search(self):
        for i in range(len(self.list)):
            if self.n == list[i]:
                print("found {0} in".format(list[i]) + str(i))
                break
        else:
            print("Not found")

list=[]
for i in range(5):
    f=int(input("Enter {0} value".format(i+1)))
    list.append(f)
n=int(input("search for:"))

n1=linear(list,n)
n1.search()"""

"""class binary:
    def __init__(self,list,n):              #Binarysearch using classes
        self.list=list
        self.n=n

    def search(self):
        self.list.sort()
        if self.list[0]==n or self.list[len(list)-1]==n:
            print("{0} found ".format(n))
            print(self.list[len(list)-1])
            print(self.list[0])
        else:
            l=globals()['l']
            u=globals()['u']
            while l<=u:
                mid=(l+u)//2
                if self.list[mid]==n:
                    print("found {0} at {1}".format(n,mid))
                    break
                else:
                    if self.list[mid]<n:
                        l=mid
                    else:
                        u=mid
list=[]
for i in range(5):
    f=int(input("Enter {0} value".format(i+1)))
    list.append(f)
n=int(input("search for:"))
l=0
u=len(list)-1

n1=binary(list,n)
n1.search()"""

"""list=[45,6,3,9,20,5]
def bubble():                               #bubble sort
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    print(list)

bubble()"""

list=[23,45,65,76,8,98]
def selection():                    #selection sort
    for i in range(len(list)):
        min=i
        for j in range(i,6):
            if list[j]<list[min]:
                min=j
        list[i],list[min]=list[min],list[i]
        print(list)
selection()
print(list)







