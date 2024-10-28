
# Megic methods 

# __len__  <-- for len()
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i += 1
#         return i
    

# e1 = Employee("Rahul")
# print(len(e1))



# # __str__  <-- This is used for return the string when only object pass as parameter in print()
# class Employee:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f'The Emlpoyee name is {self.name}'
    
    
# e2 = Employee("harry")
# print(e2)  # here without __str__ method give the address of the Employee class and that object




# __call__ <-- This used for call the objects like function 

class Employee:
    def __call__(self):
        print("This is used as function")

e3 = Employee()
e3()   # using this __call__ we can call the objects 
