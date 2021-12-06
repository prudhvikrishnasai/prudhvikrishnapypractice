from spV1 import *
def fun1():
    add()
    print("a is a"+__name__)
def fun2():
    print("b is b"+__name__)            #__name__ and __main__
def main():
    fun1()
    fun2()
main()
