def getLargestFactor(n: int | float) -> int:
    divisor = 2
    while n % 2 == 0:
      n /= 2

    divisor = 3
    while n > 1:
      if n % divisor == 0:
          n /= divisor
      else: divisor += 2
    return divisor

n = 600851475143
print(getLargestFactor(n))
