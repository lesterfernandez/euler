import math

def PythTp_sumconstraint(n: int) -> list[int] | None:
    for a in range(1, n - 1):
        if a > n / 2: return None
        for b in range(a + 1, n - a - 1):
            if a * a + b * b == (n-a-b) * (n-a-b):
                return [a, b, n-a-b]


nums = PythTp_sumconstraint(1000) or []
print(math.prod(nums))


