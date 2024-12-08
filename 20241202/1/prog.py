import sys

head = sys.stdin.buffer.read(1)
N = head[0]
tail = sys.stdin.buffer.read().rstrip(b'\r\n')
L = len(tail)

parts = [
    tail[int(i * L / N):int((i + 1) * L / N)]
    for i in range(N)
]

sorted_parts = b''.join(sorted(parts))

sys.stdout.buffer.write(head + sorted_parts)
sys.stdout.buffer.flush()
