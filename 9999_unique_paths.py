from math import factorial as f

# find unique paths coding challenge #1 from bitburner
# m: rows, n: columns

def uniquePath(m: int, n: int) -> int:
    return int(f(m + n - 2) / (f(m - 1) * f(n-1)))

print(uniquePath(3,11))
