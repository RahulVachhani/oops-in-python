
# Inheritance

# class Animal:

#     def feature1(self):
#         print("The feature 1 in class Animal ")

# class Dog(Animal):

#     def feature2(self):
#         print("The feature 2 in class Dog")

# d1 = Dog()
# d1.feature1()   
# d1.feature2()



# Single level

# class Animal:
#     def __init__(self):
#         print("Class Animal")

#     def feature1(self):
#         print("The feature 1 in class Animal ")

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Class Dog")

#     def feature2(self):
#         print("The feature 2 in class Dog")

# d1 = Dog()
# d1.feature1()
# d1.feature2()
   


class Animal:
    def __init__(self):
        print("Class Animal")

    def feature1(self):
        print("The feature 1 in class Animal ")

class Dog:
    def __init__(self):
        print("Class Dog")

    def feature1(self):
        print("The feature 1 in class Dog")


class Lion(Animal, Dog):
    def __init__(self):
        super().__init__()
        print('Class Lion')

    def feature2(self):
        print("The feature 2 in class lion")

l1 = Lion()
l1.feature1()   # its print Animal Class feature1() method beacuse in multiple inheritance its going to left to right
   
 

# mro() is diplay all the order of inheritance
print(Lion.mro())
