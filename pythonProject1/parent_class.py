class calculator1:
    num=100 # class variables
    # default constructor - init is the default constructor in python
    def __init__(self,a,b):
        self.firstnumber = a      # Class Instance variables
        self.secondnumber = b
        print("I am called automatically when function is called")
    def getData(self):
        print("I am now executing as method in class")
    def summation(self):
        return self.firstnumber + self.secondnumber + calculator1.num

obj = calculator1(2,3)      # Syntax to create objects in python
obj.getData()
print(obj.summation())

obj = calculator1(4,5)      # Syntax to create objects in python
print(obj.summation())