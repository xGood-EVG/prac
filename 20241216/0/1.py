import asyncio


async def squarer(value):
    return value ** 2


async def doubler(value):
    return value * 2


async def main(numbers):
    sqr = await asyncio.gather(*(squarer(n) for n in numbers))
    mult = await asyncio.gather(*(doubler(n) for n in sqr))
    print(mult)

asyncio.run(main([9, 10]))