import asyncio

# A shared variable
shared_resource = 0

# An asyncio Lock
lock = asyncio.Lock()
#to ensure that no 2 coroutine a accessing a data at same time
async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1  # Modify the shared resource
        await asyncio.sleep(1)  # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical section ends

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

asyncio.run(main())
