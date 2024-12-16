import asyncio

evsnd, evmid = asyncio.Event(), [asyncio.Event(), asyncio.Event()]

async def send(ev, name, evname):
    ev.set()
    print(f"{name}: generated {evname}")


async def recv(ev, name, evname):
    ev.set()
    print(f"{name}: recieved {evname}")


async def snd():
    await send(evsnd, "snd", "evsnd")


async def mid(n):
    await recv(evsnd, f"mid{n}", "evsnd")
    await send(evmid[n], f"mid{n}")