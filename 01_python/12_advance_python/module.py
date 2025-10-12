def myFunc():
    print("Hello world!")

myFunc()
print(__name__)


if __name__ == "__main__":
    #
    print("we are directly running this code")
    myFunc()
    print(__name__)
    