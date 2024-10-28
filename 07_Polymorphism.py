

# Polymorphism


# Duck Typing

class Vscode:

    def execute(self):
        print("Execute VScode")

class PyCharm:

    def execute(self):
        print("Execute Pycharm")

class Laptop:

    def execute(self, ide):
        ide.execute()

v1 = Vscode()

l1 = Laptop()
l1.execute(v1)

p1 = PyCharm()
l1.execute(p1)
