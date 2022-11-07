import math
import time
start_time = time.perf_counter()

# O(n*m) time
# O(n*m) space
# GETS MAX PRODUCT (WITH WINDOW)

def buildMatrixFromFile(file_name: str) -> list[list[int]]:
    file = open(file_name)
    matrix = []
    for line in file:
        row = line.rstrip().split(" ")
        parsed_row = list(map(int, row))
        matrix.append(parsed_row)
    file.close()
    return matrix


def getLargestWindow(windows: list[list[int]]) -> tuple[int, list[int]]:
    max_product = 1
    max_window = [1, 1, 1, 1]
    for window in windows:
        product = math.prod(window)
        if product > math.prod(max_window):
            max_window = window
            max_product = product
    return max_product, max_window

def maxNProductInMatrix(matrix: list[list[int]], n: int) -> tuple[int, list[int]]:
    def buildHorizontal(row: list[int], colIdx: int, n: int) -> list[int]:
        return row[colIdx : colIdx + n]

    def buildVertical(rowIdx: int, colIdx: int, n: int) -> list[int]:
        vertical = []
        for k in range(n):
            vertical.append(matrix[rowIdx + k][colIdx])
        return vertical

    def buildDiagonals(rowIdx: int, colIdx: int, n: int) -> tuple[list[int], list[int]]:
        diagonalDown = []
        diagonalUp = []
        for k in range(n):
            diagonalDown.append(matrix[rowIdx + k][colIdx + k])
            diagonalUp.append(matrix[rowIdx + n - 1 - k][colIdx + k])
        return diagonalDown, diagonalUp

    max_product = 1
    max_window = []
    for rowIdx, row in enumerate(matrix):
        for colIdx, _ in enumerate(row):
            horizontal: list[int] = []
            vertical: list[int] = []
            diagonalDown: list[int] = []
            diagonalUp: list[int] = []

            if rowIdx <= len(matrix) - n and colIdx <= len(row) - n:
                horizontal = buildHorizontal(row, colIdx, n)
                vertical = buildVertical(rowIdx, colIdx, n)
                diagonalDown, diagonalUp = buildDiagonals(rowIdx, colIdx, n)
            elif rowIdx <= len(matrix) - n:
                vertical = buildVertical(rowIdx, colIdx, n)
            elif colIdx <= len(row) - n:
                horizontal = buildHorizontal(row, colIdx, n)

            product, window = getLargestWindow([horizontal, vertical, diagonalDown, diagonalUp])
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
