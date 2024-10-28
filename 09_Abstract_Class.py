
# Abstract Class

from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def show(self):
        pass

class Dell(Computer):

    def show(self):
        print('The Dell Computer')


# This will gives an error beacuse we can not create object of abstract class 
# c1 = Computer()
# c1.show()

c1 = Dell()
c1.show()