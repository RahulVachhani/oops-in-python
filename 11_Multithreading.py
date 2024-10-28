
# Multithreading


# from threading import *
# from time import sleep       # For interval

# class Hello(Thread):
#     def run(self):
#         for i in range(100):
#             print("Hello")
#             sleep(1)
    
# class Hi(Thread):
#     def run(self):
#         for i in range(100):
#             print("Hi")
#             sleep(1)
# h1 = Hello()
# h1.start()

# c1 = Hi()
# c1.start()

# c1.join()
# h1.join()

# print("Main Thread")



# Code with Harry

import threading
import time

def funct1(second):
    print(f'The function 1 is sleep for {second} second')
    time.sleep(second)


# This is run normaly
# time1 = time.perf_counter()
# funct1(3)
# funct1(2)
# funct1(1)
# time2 = time.perf_counter()
# print(time2 - time1)    # its take 1 + 2 + 3 = 6 seconnd

# By threading 
time1 = time.perf_counter()

t1 = threading.Thread(target=funct1, args=[3])
t2 = threading.Thread(target=funct1, args=[2])
t3 = threading.Thread(target=funct1, args=[1])

t1.start()
t2.start()
t3.start()


time2 = time.perf_counter()
print(time2 - time1)    # its start concurrently so time takes 0 seconds


 

