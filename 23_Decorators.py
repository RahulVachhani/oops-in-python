
# Decorators 

def addition(fun):
    def wrapper(*n):
        print(f"The addition perform of {n}")
        fun(*n)
    return wrapper

@addition
def add(a,b):
    print(f"addition : {a+b}")

add(10,20)

# addition(add)(1,2)
