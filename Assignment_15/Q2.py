# 2. Create a class Product with members as pid,pname,price and quantity.
# Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:


    def __init__(self, pid = 0 , pname = 'Unknown' , price = 0.0 , quantity = 'Unkonwn'):
        self.pid = pid
        self.pname = pname
        self.price = price 
        self.quanity = quantity


    def __del__(self):
        print("Product object distroyed.")

    def ShowBook(self):
        print('Product Id :' , self.pid)
        print('Product Name :', self.pname)
        print('Product Price :', self.price)
        print('Product Quanity :', self.quanity)

p1 = Product()
p1.ShowBook()

print('========================')

p2 = Product(102 , 'Automic Habit' , 999.00 , 5)
p2.ShowBook()


print('========================')