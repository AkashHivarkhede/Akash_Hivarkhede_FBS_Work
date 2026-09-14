# Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.



class Shirt:

  
    size_increase = 10

   
    def __init__(self, sid=0, sname="", type="", price=0, size=""):

        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt object destroyed")

  
    def ShowBook(self):
        print("Shirt ID   :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type       :", self.type)
        print("Price      :", self.price)
        print("Size       :", self.size)


    def calculate_price(self):

        if self.size == "small":
            self.price = self.price

        elif self.size == "medium":
            self.price = self.price + (self.price * Shirt.size_increase / 100)

        elif self.size == "large":
            self.price = self.price + (self.price * Shirt.size_increase * 2 / 100)

        elif self.size == "xlarge":
            self.price = self.price + (self.price * Shirt.size_increase * 3 / 100)

        else:
            print("Invalid size")



s1 = Shirt(101, "Formal Shirt", "Formal", 1000, "small")
s2 = Shirt(102, "Formal Shirt", "Formal", 1000, "medium")
s3 = Shirt(103, "Formal Shirt", "Formal", 1000, "large")
s4 = Shirt(104, "Formal Shirt", "Formal", 1000, "xlarge")




s1.calculate_price()
s2.calculate_price()
s3.calculate_price()
s4.calculate_price()




s1.ShowBook()
print()

s2.ShowBook()
print()

s3.ShowBook()
print()

s4.ShowBook()
