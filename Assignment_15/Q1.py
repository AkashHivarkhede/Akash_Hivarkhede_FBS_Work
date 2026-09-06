# 1. Create a class Book with members as bid,bname,price and author.
# Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook


class Book:

    def __init__(self , bid = 0 , bname = 'Unknown' , price = 0.0 , author = 'Unknown'):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print('Book object distroyed.')


    def ShowBook(self):
        print('Book Id :', self.bid)
        print('Book Name :' , self.bname)
        print('Prince :', self.price)
        print('Author :', self.author)

book1 = Book()
book1.ShowBook()

print("-----------------------")

book2 = Book(101 , 'Automic Habbit' , '899.00' , 'John Smith')
book2.ShowBook()

print("-----------------------")

