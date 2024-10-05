

# Importing from parent class in parent_class.py file
from parent_class import calculator1


class ChildImp1(calculator1):   # Child class (ChildImp1) inheriting from parent class (calculator1)
    num2= 200

    def __init__(self):
        calculator1.__init__(self,100,10)

    def getcompleteData(self):
        return self.num2 + self.num + self.summation()

obj = ChildImp1()
print(obj.getcompleteData())

