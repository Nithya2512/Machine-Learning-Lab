def pairs(arr,n):
    count=0
    for i in arr:
        arr.remove(i)
        if (n-i) in arr:
            count+=1
    return count
arr=list(map(int,input().split()))
n=int(input("The sum you want:"))
count=pairs(arr,n)
print(count)