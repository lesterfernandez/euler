import time
start_time = time.perf_counter()

from p5_smallest_multiple import getPrimeFactors
def numOfDivisors(n: int):
    factorPowers = getPrimeFactors(n)
    num = 1
    for power in factorPowers.values():
        num *= power + 1
    return num

def firstTriangular(d: int):
    index = 1
    current = index
    while numOfDivisors(current) < d:
        index += 1
        current += index
    return current

print(firstTriangular(500))

end_time = time.perf_counter()
print(f"It took {(end_time - start_time):.3f}s")
