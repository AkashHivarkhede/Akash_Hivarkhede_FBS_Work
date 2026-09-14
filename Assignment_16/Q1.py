# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.


class Book:

    count = 0

    def __init__(self , bid = 0 , bname ='Unknown' , price = 0.0 , author = 'Unknown'):
        self.bid = bid
        self.bname = bname
        self.price = price 
        self.author = author

        Book.count += 1

    def __del__(self):
        print('Book object distroyed.')

    def ShowBook(self):
        print('Book Id :', self.bid)
        print('Book Name :' , self.bname)
        print('Prince :', self.price)
        print('Author :', self.author)



b1 = Book(101 , 'Automic Habbit' , '899.00' , 'John Smith')
b2 = Book(102 , 'Rich Dad Poor Dad' , '499.00' , 'Robert Kiyosaki')
b3 = Book() 

b1.ShowBook()
print("-----------------------")

b2.ShowBook()
print("-----------------------")


b3.ShowBook()
print("-----------------------")

print('Total Book Objects Created :', Book.count)