class MyClass():
    def method1(self):
        print("in MyClass")

    def __init__(self):
        print("In init MyClass")

class ChildClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("In child class")

    def method2(self):
        print("In child class method2")

    def __init__(self, name):
        MyClass.__init__(self)
        self.name = name


def main():
    print("In main")
    c = ChildClass("child")
    c.method1()
    c.method2()

if __name__ == "__main__":
    main()
