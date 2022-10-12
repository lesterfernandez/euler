# Time complexity: O(n^2)
# Space complexity: O(n)

primes = [2]
current = 3
while len(primes) < 10001:
    #  Using list comprehension:
    #  primeNotFactors = [n for n in primes if current % n != 0]
    #  if len(primeNotFactors) == len(primes): # none of the primes were a factor
    #      primes.append(current)
    #  current += 2

    for n in primes:
        if current % n == 0:
            break
    else: # if we did not break the loop
        primes.append(current)
    current += 2

print(f"THE ANSWER IS: {primes[-1]}")
