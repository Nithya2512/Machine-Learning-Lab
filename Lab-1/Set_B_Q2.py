def mul(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = []
B = []
AM = int(input("Rows of A: "))
AN = int(input("Columns of A: "))
BM = int(input("Rows of B: "))
BN = int(input("Columns of B: "))
print(f"Enter {AM} rows for Matrix A (space-separated numbers):")
for i in range(AM):
    row = list(map(int, input().split()))
    A.append(row)
print(f"Enter {BM} rows for Matrix B (space-separated numbers):")
for i in range(BM):
    row = list(map(int, input().split()))
    B.append(row)
if AN == BM:
    result = mul(A, B)
    print("\nResult matrix:")
    for row in result:
        print(row)
else:
    print("The two matrices cannot be multiplied.")