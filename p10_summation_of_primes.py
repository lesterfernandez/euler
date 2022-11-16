import math

def sumOfPrimesBelowN(n: int) -> int:
    primes = [2]
    sum = 2
    current = 3
    while current < n:
        for prime in primes:
            if current % prime == 0:
                break
            if prime > math.sqrt(current):
                primes.append(current)
                sum += current
                break
        current += 2
    return sum


print(sumOfPrimesBelowN(2_000_000))
