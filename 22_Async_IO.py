
# Asyncronization and Wait

import asyncio

async def func1():
    print("Function 1 is start")
    await asyncio.sleep(2)
    print("Function 1")

async def func2():
    print("Function 2 is start")
    await asyncio.sleep(1)
    print("Function 2")

async def func3():
    print("Function 3 is start")
    await asyncio.sleep(4)
    print("Function 3")

async def main():
    # this is used for concurrent run the function 
    # 3 function are run concurrently its not wait for any other function execution
    l = await asyncio.gather(         
        func1(),
        func2(),
        func3()
    )
    print(l)  # this will print the return value of functions in await asyncio.gather
    print("All the funtions are executed")  # after all the function are executes then after the rest of the code will executes

asyncio.run(main())
