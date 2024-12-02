import struct
import random

filename = "file.bin"

with open(filename, "wb") as f:
    for _ in range(10):
        rnd_float = random.uniform(-1000.0, 1000.0)
        rnd_bytes = bytes(random.choices(range(256), k=3))
        rnd_int = random.randint(-1000, 1000)

        data = struct.pack("f3si", rnd_float, rnd_bytes, rnd_int)

        f.write(data)