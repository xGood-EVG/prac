import asyncio


async def prod(s1):
    for i in range(5):
        value = f"value_{i}"
        await s1.put(value)
        print(f"prod: put {value} to s1")
        await asyncio.sleep(1)
    print("prod: finished producing")


async def mid(s1, s2):
    while True:
        value = await s1.get()
        print(f"mid: got {value} from s1")
        await s2.put(value)
        print(f"mid: put {value} to s2")


async def cons(s2):
    while True:
        value = await s2.get()
        print(f"cons: got {value} from s2")


async def main():
    s1 = asyncio.Queue()
    s2 = asyncio.Queue()

    pt = asyncio.create_task(prod(s1))
    mt = asyncio.create_task(mid(s1, s2))
    ct = asyncio.create_task(cons(s2))

    await pt

asyncio.run(main())