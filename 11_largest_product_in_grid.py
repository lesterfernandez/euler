import time
start_time = time.perf_counter()

# O(n) time
# O(1) space
# GETS MAX PRODUCT (NO WINDOW)

def buildMatrixFromFile(file_name: str) -> list[list[int]]:
    file = open(file_name)
    matrix = []
    for line in file:
        row = line.rstrip().split(" ")
        parsed_row = list(map(int, row))
        matrix.append(parsed_row)
    file.close()
    return matrix

def maxNProductInMatrix(matrix: list[list[int]], n: int) -> int:
    max_product = 1
    for rowIdx, row in enumerate(matrix):
        for colIdx, _ in enumerate(row):
            horizontal = 1
            vertical = 1
            diagonalDown = 1
            diagonalUp = 1
            for k in range(n):
                if colIdx + n <= len(row):
                    horizontal *= row[colIdx + k]

                if rowIdx + n <= len(matrix):
                    vertical *= matrix[rowIdx + k][colIdx]

                if colIdx + n <= len(row) and rowIdx + n <= len(matrix):
                    diagonalDown *= matrix[rowIdx + k][colIdx + k]
                    diagonalUp *= matrix[rowIdx + n - 1 - k][colIdx + k]

            max_product = max(horizontal, vertical, diagonalDown, diagonalUp, max_product)
    return max_product

matrix = buildMatrixFromFile("./11_input.txt")
result = maxNProductInMatrix(matrix, 4)
print(result)

# Performance timer
end_time = time.perf_counter()
print(f"it took : {(end_time - start_time) * 1000:0.3f}ms")
