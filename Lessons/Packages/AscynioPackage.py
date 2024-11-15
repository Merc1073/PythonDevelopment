import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)
    print("...World!")

asyncio.run(say_hello())


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    # Run both tasks concurrently
    await asyncio.gather(task1(), task2())

asyncio.run(main())



async def task3():
    print("Task 3 started")
    await asyncio.sleep(2)
    print("Task 3 finished")


async def task4():
    print("Task 4 started")
    await asyncio.sleep(1)
    print("Task 4 finished")


async def main():
    # Create individual tasks
    t3 = asyncio.create_task(task3())
    t4 = asyncio.create_task(task4())

    print("Tasks have been created and are running...")

    # Wait for both tasks to complete
    await t3
    await t4


asyncio.run(main())


