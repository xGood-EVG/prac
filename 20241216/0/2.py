import asyncio


async def squarer(value):
    return value ** 2


async def doubler(value):
    return value * 2


async def main(numbers):
    async with asyncio.TaskGroup() as tg:
        sqr_task = [tg.create_task(squarer(n)) for n in numbers]

    squared = [tmp1.result() for tmp1 in sqr_task]
    async with asyncio.TaskGroup() as tg:
        mlt_task = [tg.create_task(doubler(n)) for n in squared]
    
    return list(tmp.result() for tmp in mlt_task)

print(asyncio.run(main([2, 3])))