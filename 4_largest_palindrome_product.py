def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    return True

def getLargestPalindrome(n):
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
    return [palindrome, factors]


n = input("Number of digits for largest palindrome: ")
while not n.isdigit():
    n = input("Please enter an integer: ")
print(getLargestPalindrome(int(n)))
