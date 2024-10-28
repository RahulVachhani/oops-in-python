
# Operator Overloading


class A:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def show(self):
        print(self.m1, self.m2)

        
    # Operator Overloading
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        return m1, m2
    
    def __mul__(self, other):
        m1  = self.m1 * other.m1
        m2 = self.m2 * other.m2

        return m1, m2

s1 = A(20,30)
s2 = A(40,20)

s3 = s1 + s2
print(s3)

s4 = s1 * s2
print(s4)

