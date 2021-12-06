def add():
    print("add is done"+__name__)
def sub():
    print("sub is done"+__name__)
def main():                     #__name__ and __main__
    add()
    sub()
if __name__=="__main__":
    main()