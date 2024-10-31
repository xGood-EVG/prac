def fib(m, n): 
    a, b = 1, 1
    for i in range(m + n): 
        if i >= m: 
            yield a 
        a, b = b, a + b 

import sys
exec(sys.stdin.read())
