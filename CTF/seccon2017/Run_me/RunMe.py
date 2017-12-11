import sys
# from lru-cache import lru_cache
import functools
sys.setrecursionlimit(99999)

@functools.lru_cache(maxsize=1000)
def f(n):
    if n < 2:
        return n 
    else:
        return f(n-2) + f(n-1)

print(str(f(11011))[:32])

