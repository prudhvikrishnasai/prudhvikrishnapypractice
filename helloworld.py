print('Hello World!')
print('hello "krish" how are you')
greeting='hello'
name=input('please enter name')
print(greeting +' '+ name)
print("this is his's phone")
print(2+3)
print(10/2)
print(2/5/10)
parrot="Norwegian Blue"
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])
print(parrot[4-13], parrot[4])
print(parrot[0:6])
print(parrot[3:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[:])
print(parrot[:6]+parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2])
print(parrot[0:6:3])
number1= 9,234,345,654,234,678
seperator1=number1[1::4]             #slice
print(seperator1)

number= "9,234,345,654,234,678"
seperator=number[1::4]
print(seperator)
values="".join(char if char not in seperator else " " for char in number).split()
print([int(val) for val in values])
      # 01234567890123456789012345
letter="abcdefghijklmnopqrstuvwxyz"
backward_without_a= letter[26:0:-1]
backward_with_a= letter[26::-1]
forward_with_a= letter[-26::1]
forward_without_a= letter[-25::1]
backward= backward_without_a + " " + backward_with_a +" " + forward_with_a+" "+ forward_without_a
print(backward)
print(letter[::-1])
print(letter[::1])
print(letter[-1:-9:-1])
print(letter[-10:-13:-1])
print(letter[4::-1])
print("he ""is " "a " "good ""boy"".")
today="friday"
print("day" in today )  #true
print("fri" in today )  #true
print("frip" in today )  #false
print("hello "*5)
print("hello "*(5+4))
print("hello "*5 + "4")
age=24
print("my age is "+ str(age) + " years")
print("my age is {0} years".format(age))
print("there are {0} days in {1},{2},{3} months".format(31,"jan","feb","mar"))
print(letter[24::-1])
print("jan has {2} days, feb has {0} days,mar has {2} days,apr has {1} days".format(28,30,31))
print("""jan has {2} days
feb has {0} days
mar has {2} days
apr has {1} days""".format(28,30,31))
print("hello")
age=input("enter ur age")
print(age)
for i in range(1,10):
    print("{3}:- {0:2} squared is {1:4} and {0} cubed is {2:4}".format(i,i**2,i**3,i))
print()
for i in range(1,10):
    print("{3}:- {0:2} squared is {1:<4} and {0} cubed is {2:^4}".format(i,i**2,i**3,i))
print()
print("pi value is {0}".format(22/7))
print("pi value is {0:12}".format(22/7))
print("pi value is {0:12f}".format(22/7))
print("pi value is {0:12.50f}".format(22/7))
print("pi value is {0:52.50f}".format(22/7))
print("pi value is {0:62.50f}".format(22/7))
print("pi value is {0:<72.50f}".format(22/7))
print("pi value is {0:<72.54f}".format(22/7))
print(f"pi value is {22/7}")
x=[1,2,3,4]
out=[]
for num in x:
    out.append(num**2)
print(out)


n = int(input())
for i in range(1,n+1):
    print(i,end="")    #// n=5; op: 12345 //comes the same line without gaps