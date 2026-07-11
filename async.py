import asyncio
import time

async def data(id, sec):
    print(f"id is {id}")
    await asyncio.sleep(sec) #time.sleep sleps whole code but asyncio sleeps only that couroutine
    return {id: sec}
start = time.time()
async def main():
    # Create tasks
    task1 = asyncio.create_task(data(1, 2))
    task2 = asyncio.create_task(data(2, 3))
    task3 = asyncio.create_task(data(3, 1))

    res1, res2, res3 = await asyncio.gather(task1, task2, task3) 
    # in gather if any one task fail it will not stop the whole process which may leave output wierd
    print(res1, res2, res3)
end = time.time()
asyncio.run(main())
print(end-start)
#always use aysyncio.create_task then await(matlab ab run honge) them 