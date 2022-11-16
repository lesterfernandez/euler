# O(sqrt(n))
def getPrimeFactors(n):
    factors: dict[int, int] = {} # dict: { factor: power }

    # O(log2(n))
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n /= 2

    # O(sqrt(n))
    divisor = 3
    while n > 1:
        if n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n /= divisor
        else: 
            divisor += 2

    return factors

def smallestMultiple(num_range: tuple[int, int]) -> int:
    common_factors = {}
    for i in range(num_range[0], num_range[1] + 1):
        factors = getPrimeFactors(i)
        for num, power in factors.items():
            if num not in common_factors or common_factors[num] < power:
                common_factors[num] = power
    product = 1
    for num, power in common_factors.items():
        product *= pow(num, power)
    return product


if __name__ == "__main__":
    print(smallestMultiple((1, 20)))
