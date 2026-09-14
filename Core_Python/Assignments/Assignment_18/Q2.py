# Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:

    # Constructor
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    # Destructor
    def __del__(self):
        print("Distance object destroyed")

    # Overload + operator
    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm

        # Convert cm into meters
        if cm >= 100:
            m = m + cm // 100
            cm = cm % 100

        # Convert meters into kilometers
        if m >= 1000:
            km = km + m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    # Overload - operator
    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        total = total1 - total2

        km = total // 100000
        total = total % 100000

        m = total // 100
        cm = total % 100

        return Distance(km, m, cm)

    # Display
    def Display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")


# Create objects
d1 = Distance(5, 750, 80)
d2 = Distance(2, 500, 50)

# Addition
d3 = d1 + d2

print("Addition:")
d3.Display()

# Subtraction
d4 = d1 - d2

print("Subtraction:")
d4.Display()