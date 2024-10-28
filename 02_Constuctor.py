

# __init__   (Constuctor)

class Laptop:

    def __init__(self, Ram, proccesor):         # Its automaticaly executes when new objects is created
        self.Ram = Ram
        self.proccesor = proccesor

    def detail(self):
        print(f'The Ram is {self.Ram}')
        print(f'The proccesor is {self.proccesor}')


asus = Laptop('8 GB', 'i5')
asus.detail()

