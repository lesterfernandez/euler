# Time complexity: O(n^2)
# Space complexity: O(n)
def getNthPrime(n: int) -> int:
    primes = [2]
    current = 3
    while len(primes) < n:
        for prime in primes:
            if current % prime == 0:
                break
        else: # runs if we did not break the loop
            primes.append(current)
        current += 2 
    return primes[-1]

print(f"THE ANSWER IS: {getNthPrime(10001)}")
