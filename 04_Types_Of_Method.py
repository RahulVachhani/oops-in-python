

# Types Of Methods

# 1) Instance Method
# 2) Class Method
# 3) Static Method


class Student:

    college_name = "LDRP"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Instance Method <-- in which method use instance variable then that method is called as Instance Methods

    def show(self):
        print(f'The name is {self.name} and id is {self.id}')



    # Class Method <-- in which method use only class level variable then that method is called as Class Methods
    
    @classmethod    
    def get_clg_name(cls):
        print(f'The college name is {cls.college_name}')


    # Static Method  <-- this is not specific any objects or class but when we use some function then its called ad static methods
    
    @staticmethod
    def anything():
        print("This is static method")
    

s1 = Student("Rahul",10)
s1.show()
Student.get_clg_name()
Student.anything()
s1.anything()
    

        