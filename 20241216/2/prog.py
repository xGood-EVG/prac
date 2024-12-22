import asyncio


async def merge(A1, B, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(event_in1.wait(), event_in2.wait())

    i = start
    j = middle
    k = start
    while i < middle or j < finish:
        if j >= finish:
            B[k] = A1[i]
            i += 1
        elif i >= middle:
            B[k] = A1[j]
            j += 1
        elif A1[i] <= A1[j]:
            B[k] = A1[i]
            i += 1
        elif A1[j] < A1[i]:
            B[k] = A1[j]
            j += 1

        k += 1

    event_out.set()

async def mtasks(A):
    n = len(A)

    local_A = []
    B = []

    tasks = []
    events = []

    for i in range(n + 1):
        if i < n:
            local_A.append(A[i])
            B.append(0)

        events.append(asyncio.Event())
        events[-1].set()

    l = 1
    fl = True
    while l < n:
        new_events = []

        mid, fin = 0, 0
        for j in range(0, n, l * 2):
            if fin == n:
                break

            event = asyncio.Event()
            
            mid = min(j + l, n - 1)
            fin = min(j + l * 2, n)

            ev1 = events.pop(0)
            ev2 = events.pop(0)

            if fl:
                tasks.append(asyncio.create_task(merge(local_A, B, j, mid, fin, ev1, ev2, event)))
            else:
                tasks.append(asyncio.create_task(merge(B, local_A, j, mid, fin, ev1, ev2, event)))

            events.append(event)

        events.append(events[-1])
        fl = not fl
        l *= 2

    if fl:
        return tasks, local_A

    return (tasks, B)


import sys
exec(sys.stdin.read())