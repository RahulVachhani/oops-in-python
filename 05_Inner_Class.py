
# Inner Class

class Student:

    def __init__(self,name, id, cname):
        self.name = name
        self.id = id
        self.cname = self.college(cname)

    def show(self):
        print(f'The name is {self.name} ans {self.id}')
        self.cname.show()


    class college:

        def __init__(self,name):
            self.name = name

        def show(self):
            print(f'The college name is {self.name}')


s1 = Student('rahul', 10, 'LD')
s1.show()
            
