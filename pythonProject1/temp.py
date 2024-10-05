l=10
while(l>0):
    if(l==7):
        l=l-1
        continue
    if(l==2):
        l=l-1
        continue
    print(l)
    l=l-1


# CLASS EXAMPLES
class wisher:
    time = 100
    def morning(self):
        print("Good morning")
    def afternoon(self):
        print("Good afternoon")
    def evening(self):
        print("Good evening")

obj=wisher()
obj.evening()
obj.morning()
print(obj.time)


class Product:
    def __init_(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def show_price(self):
        print("The price of {} is ${}.".format(self.name, self.price))

#george_foreman = Product("Fit Medium Health Grill", 39.99, "George Foreman")



class subtractor:
    def __init__(self,a,b):
        self.firstvar=a
        self.secondvar=b
    def subtraction(self):
        return self.firstvar - self.secondvar


obj = subtractor(4,5)
print(obj.subtraction())
