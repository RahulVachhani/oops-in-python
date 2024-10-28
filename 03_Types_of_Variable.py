

# Types Of Variable

# 1) instance variable
# 2) class level variable 

class Student:
    # Class Level Variable (Shared by all instances)
    college_name = "LDRP"


    def __init__(self, name, id):
        self.name = name  # Instance Variable
        self.id = id      


# Accessing the Class Level Variable without creating any objects
print(Student.college_name)  # Output: LDRP


s1 = Student('Rahul', 10)

# Accessing the Instance Variable
print(s1.name)


# Accessing the Class Level Variable using the object (not recommended but works)
print(s1.college_name)  

#
