def getStringsFromFile(file_name: str) -> list[str]:
    file = open(file_name)
    matrix = [line.rstrip() for line in file]
    file.close()
    return matrix

def firstNDigitSum(n: int, num_strings: list[str]) -> str:
    digits = len(num_strings[0])
    sum = 0
    output = []
    for col in range(0, digits):
        for row in num_strings:
            index = digits - col - 1
            sum += int(row[index])
        remainder = sum % 10
        sum = (sum - remainder) // 10
        output.append(str(remainder))
    while sum > 0: 
        remainder = sum % 10
        sum = (sum - remainder) // 10
        output.append(str(remainder))
    return "".join(output[-n:][::-1])

num_strings = getStringsFromFile("p13_input.txt")
print(firstNDigitSum(10, num_strings))
