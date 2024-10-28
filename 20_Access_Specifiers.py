
# In python there no any concept like public, private and protected

# But in python there like assume private and protected


# Private variable --> Private is define by '__' (double underscore)

class Employee:
    def __init__(self):
        self.__name = "Raj"

e1 = Employee()
# print(e1.__name)    # This will give error we can not access private variable out side the class


# but we can access private variable in directly by this :
print(e1._Employee__name)

# print(e1.__dir__())  # This will shiow all the method which is executable is e1 object


e1._Employee__name = "Ronak"  # we can now change it
print(e1._Employee__name) 







# Protected Variable  --> This varibale define by _ (single underscore)

class Teacher:
    def __init__(self):
        self._name = "Alakh"

t1 = Teacher()
print(t1._name)  # we can access directaly outside the class but using _ (single underscore) we assume that that is protected variable in python.


