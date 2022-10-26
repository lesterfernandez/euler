from collections import deque

def maxDigitProductFromFile(file_name: str, n: int) -> int:
    f = open(file_name, "r")
    max_product = 0
    product = 1
    window = deque([])
    for line in f:
        for char in line.rstrip():
            num = int(char)
            if num == 0:
                window.clear()
                product = 1
                continue
            if len(window) < n:
                window.append(num)
                product *= num
            else:
                head = window.popleft()
                window.append(num)
                product = (product / head) * num
                if product > max_product:
                    max_product = product
    return max_product

result = maxDigitProductFromFile("./8_input.txt", 13)
print(result)
