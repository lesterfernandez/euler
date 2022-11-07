import math

def buildMatrixFromFile(file_name: str) -> list[list[int]]:
    file = open(file_name)
    matrix = []
    for line in file:
        row = line.rstrip().split(" ")
        parsed_row = list(map(int, row))
        matrix.append(parsed_row)
    file.close()
    return matrix

def largestProductFromLists(windows: list[list[int]]) -> int:
    max_product = 1
    for window in windows:
        max_product = max(max_product, math.prod(window))
    return max_product

def maxNProductInMatrix(matrix: list[list[int]], n: int) -> int:
    def buildHorizontal(row: list[int], colIdx: int, n: int) -> list[int]:
        return row[colIdx : colIdx + n]

    def buildVertical(rowIdx: int, colIdx: int, n: int) -> list[int]:
        vertical = []
        for k in range(n):
            vertical.append(matrix[rowIdx + k][colIdx])
        return vertical

    def buildDiagonalDown(rowIdx: int, colIdx: int, n: int) -> list[int]:
        diagonalDown = []
        for k in range(n):
            diagonalDown.append(matrix[rowIdx + k][colIdx + k])
        return diagonalDown

    def buildDiagonalUp(rowIdx: int, colIdx: int, n: int) -> list[int]:
        diagonalUp = []
        for k in range(n - 1, -1, -1):
            diagonalUp.append(matrix[rowIdx + k][colIdx + n - 1 - k])
        return diagonalUp

    max_product = 1
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            horizontal: list[int] = []
            vertical: list[int] = []
            diagonalDown: list[int] = []
            diagonalUp: list[int] = []
            if i <= len(matrix) - n and j <= len(row) - n:
                horizontal = buildHorizontal(row, j, n)
                vertical = buildVertical(i, j, n)
                diagonalDown = buildDiagonalDown(i, j, n)
                diagonalUp = buildDiagonalUp(i, j, n)
            elif i <= len(matrix) - n:
                vertical = buildVertical(i, j, n)
            elif j <= len(row) - n:
                horizontal = buildHorizontal(row, j, n)

            product = largestProductFromLists([horizontal, vertical, diagonalDown, diagonalUp])
            max_product = max(max_product, product)
    return max_product

matrix = buildMatrixFromFile("./11_input.txt")
result = maxNProductInMatrix(matrix, 4)
print(result)
