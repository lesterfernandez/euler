import math

# O(sqrt(n))
def numberOfFactors(n: int):
    count = 0
    max_factor = int(math.sqrt(n))
    if n % math.sqrt(n) == 0: count += 1
    for i in range(1, max_factor):
        if n % i == 0:
            count += 2 # factors i and n/i
    return count

# O(n^(3/2))
def findTriangleNumber(factors: int):
    current = 1
    index = 1
    while numberOfFactors(current) < factors:
        index += 1
        current += index
    return current
    
print(findTriangleNumber(500))
