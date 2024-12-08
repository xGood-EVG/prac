import sys
sys.getdefaultencoding()

while s := sys.stdin.buffer.read().decode('utf-8', errors='replace'):
    print(s.encode('latin1', errors='replace').decode('cp1251', errors='replace'))