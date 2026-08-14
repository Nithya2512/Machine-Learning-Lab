def transpose(A):
    result=[[row[i] for row in A] for i in range(len(A[0]))]
    return result

m=int(input("Enter the number of rows:"))
n=int(input("Enter the number of columns:"))
A=[]
for i in range(m):
    row=list(map(int,input().split()))
    A.append(row)
result=transpose(A)
print(result)