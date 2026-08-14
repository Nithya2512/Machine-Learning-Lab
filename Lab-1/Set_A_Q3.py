def multiply_matrices(matrix1, matrix2):
    size = len(matrix1)
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            value = 0
            for k in range(size):
                value += matrix1[i][k] * matrix2[k][j]
            row.append(value)
        result.append(row)
    return result
def matrix_power(matrix, power):
    size = len(matrix)
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
    for _ in range(power):
        result = multiply_matrices(result, matrix)
    return result

n = int(input("Enter the order of the matrix: "))
matrix = []
print("Enter the matrix elements:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
m = int(input("Enter the power: "))
answer = matrix_power(matrix, m)
print("Matrix A^", m, "is:")
for row in answer:
    print(row)