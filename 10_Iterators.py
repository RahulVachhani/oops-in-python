
# iterator  
# # for iterate use two things 1.iter() and 2.next()

# l1 = [1,2,3]

# l1 = iter(l1)
# print(next(l1))
# print(next(l1))


class A:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        val = self.num
        self.num += 1

        return val

c1 = A()
print(c1)
print(next(c1))
print(next(c1))
print(next(c1))