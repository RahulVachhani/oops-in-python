
# Getter and Setter 


class Student:

    def __init__(self,sname):
        self.sname = sname

    # @property is use for getter method
    @property 
    def name(self):
        return self.sname
    
    # @function_name.setter is use for setter method
    @name.setter
    def name(self, n):
        self.sname = n


s1 = Student("Reena")
print(s1.name)
s1.name = "Ronak"
print(s1.name)
