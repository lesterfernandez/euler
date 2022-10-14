def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) -1
    while left < right:
        if s[left] != s[right]: 
            return False
        left += 1
        right -= 1
    return True

def getLargestPalindrome(n: int) -> tuple[int, tuple[int, int]]:
    lowerBound = pow(10, n - 1)
    upperBound = pow(10, n)
    factors = (1, 1)
    palindrome = 0
    for i in range(lowerBound, upperBound):
        for j in range(i, upperBound):
            product = i * j
            if product > palindrome and isPalindrome(str(product)):
                palindrome = product
                factors = i, j
    return palindrome, factors


n = 3
print(getLargestPalindrome(int(n)))
