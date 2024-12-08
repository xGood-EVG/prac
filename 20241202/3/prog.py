import sys
import struct

raw = sys.stdin.buffer.read()
l = len(raw)

if l < 44 or raw[:4] != b'RIFF' or raw[8:16] != b'WAVEfmt ' or raw[36:40] != b'data':
    print('NO')
    exit(0)

t1 = struct.unpack("i", raw[16:20])[0]
t3 = struct.unpack("h", raw[32:34])[0]
t2 = struct.unpack("i", raw[28:32])[0]

c = struct.unpack("h", raw[22:24])[0]
r = struct.unpack("i", raw[24:28])[0]
b = struct.unpack("h", raw[34:36])[0]

if t1 != 16 or t2 != (r * b * c) / 8 or t3 != (b * c) / 8 or t3 not in {1, 2, 4}:
    print('NO')
    exit(0)

s = struct.unpack("i", raw[4:8])[0]
t = struct.unpack("h", raw[20:22])[0]
d = struct.unpack("i", raw[40:44])[0]

if s != l - 8 or r not in {44100, 4800} or d != s - 36:
    print('NO')
    exit(0) 

print(f'Size={s}, Type={t}, Channels={c}, Rate={r}, Bits={b}, Data size={d}')