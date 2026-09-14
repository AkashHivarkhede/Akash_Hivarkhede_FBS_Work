# Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero


class Television:

    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

   
    def Accept(self):

        self.model_no = int(input("Enter Model Number: "))

        if self.model_no > 9999:
            raise Exception("Model number should not be more than 4 digits")

        self.screen_size = float(input("Enter Screen Size: "))

        if self.screen_size < 12 or self.screen_size > 70:
            raise Exception("Screen size should be between 12 and 70 inches")

        self.price = float(input("Enter Price: "))

        if self.price < 0 or self.price > 5000:
            raise Exception("Price should be between 0 and 5000")


    def Display(self):
        print("\nTelevision Details")
        print("Model Number :", self.model_no)
        print("Screen Size  :", self.screen_size, "inches")
        print("Price        :", self.price, "Rs")


tv = Television()

try:
    tv.Accept()
    tv.Display()

except Exception as e:
    print("Error:", e)

    tv.model_no = 0
    tv.screen_size = 0
    tv.price = 0

    print("\nAll values are replaced with zero.")
    tv.Display()