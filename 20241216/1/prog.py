import asyncio


event = asyncio.Event()

async def writer(queue, delay):
    num = 0

    while True:
        await asyncio.sleep(delay)
        await queue.put(f'{num}_{delay}')

        if event.is_set():
            return None

        num += 1

async def stacker(queue, stack):
    while True:
        await asyncio.sleep(0)
        try:
            el = await queue.get()
            await stack.put(el)
        except Exception:
            pass

        if event.is_set():
            break

async def reader(stack, num, delay):
    while num > 0:
        await asyncio.sleep(delay)

        try:
            el = await stack.get()
        except Exception:
            break

        print(el)
        num -= 1

    event.set()


async def main():
    queue = asyncio.Queue()
    stack = asyncio.LifoQueue()

    delay1, delay2, delay3, num = eval(input())

    await asyncio.gather(
        writer(queue, delay1),
        writer(queue, delay2),
        stacker(queue, stack),
        reader(stack, num, delay3)
    )

asyncio.run(main())