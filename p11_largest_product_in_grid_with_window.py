# Gets max product and its corresponding window/block

import math
import time
start_time = time.perf_counter()

# Let n = the amount of numbers in the input matrix
# Let k = the size of the window / number of products
# Runtime complexity:
# O(n)
# Memory consumption:
# 4 lists of size k are created every iteration; We iterate n times
# O(4kn) = O(n) (k is a constant) (not including input matrix)

def buildMatrixFromFile(file_name: str) -> list[list[int]]:
    file = open(file_name)
    matrix = []
    for line in file:
        row = line.rstrip().split(" ")
        parsed_row = list(map(int, row))
        matrix.append(parsed_row)
    file.close()
    return matrix

def getLargestWindow(*windows: list[int]): # *args
    max_product = 1
    max_window = [1]
    for window in windows:
        product = math.prod(window)
        if product > max_product:
            max_window = window
            max_product = product
    return max_product, max_window

def maxNProductInMatrix(matrix: list[list[int]], n: int) -> tuple[int, list[int]]:
    def buildHorizontal(row: list[int], colIdx: int, n: int):
        return row[colIdx : colIdx + n] # list slicing

    def buildVertical(rowIdx: int, colIdx: int, n: int):
        return [ matrix[rowIdx + i][colIdx] for i in range(n) ] # list comprehension

    def buildDiagonalDown(rowIdx: int, colIdx: int, n: int):
        return [ matrix[rowIdx + i][colIdx + i] for i in range(n) ]

    def buildDiagonalUp(rowIdx: int, colIdx: int, n: int):
        return [ matrix[rowIdx + n - 1 - i][colIdx + i] for i in range(n) ]

    max_product = 1
    max_window = []
    for rowIdx, row in enumerate(matrix):
        for colIdx, _ in enumerate(row):
            horizontal = []
            vertical = []
            diagonalDown = []
            diagonalUp = []

            if rowIdx <= len(matrix) - n and colIdx <= len(row) - n:
                horizontal = buildHorizontal(row, colIdx, n)
                vertical = buildVertical(rowIdx, colIdx, n)
                diagonalDown = buildDiagonalDown(rowIdx, colIdx, n)
                diagonalUp = buildDiagonalUp(rowIdx, colIdx, n)
            elif rowIdx <= len(matrix) - n:
                vertical = buildVertical(rowIdx, colIdx, n)
            elif colIdx <= len(row) - n:
                horizontal = buildHorizontal(row, colIdx, n)

            product, window = getLargestWindow(horizontal, vertical, diagonalDown, diagonalUp)
            if product > max_product:
                max_window = window
                max_product = product
    return max_product, max_window

matrix = buildMatrixFromFile("./11_input.txt")
product, window = maxNProductInMatrix(matrix, 4)
print(f"Product: {product}")
print(f"Window: {window}")

# Performance timer
end_time = time.perf_counter()
print(f"it took : {(end_time - start_time) * 1000:0.3f}ms")
