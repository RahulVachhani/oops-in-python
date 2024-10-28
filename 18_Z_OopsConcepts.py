
class School:
    def __init__(self, sname):
        self.sname = sname

    def get_info(self):
        return f'{self.sname}'

class Teacher(School):
    def __init__(self,sname,tname,sub):
        super().__init__(sname)
        self.tname = tname
        self.sub = sub

    def get_info(self):
        return(f'School is : {super().get_info()} and teacher is : {self.tname} and Sub is : {self.sub}' )

    
class subject:
    def __init__(self):
        self.all_teacher = []

    def add_sub(self,sub):
        self.all_teacher.append(sub)
    
    def show(self):
        for sub in self.all_teacher:
            print(f'{sub.get_info()}')
    
s1 = subject()

t1 = Teacher('ld','rushi','maths')

t2 = Teacher('ldrp','kush','science')
s1.add_sub(t1)
s1.add_sub(t2)
s1.show()

