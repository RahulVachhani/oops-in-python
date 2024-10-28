
# Class


class Car:
    '''This is car class'''
    def __init__(self):
        print("Always Execute when objects are created")

    def details(self):
        print("This is car")

audi = Car()    # Create an object of Class Car
audi.details()  # Car.details(audi)    <-- This also work

porse = Car()
print(Car.__doc__)



