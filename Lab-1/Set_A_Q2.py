arr=list(map(int,input().split()))
if len(arr)>=3:
    range=max(arr)-min(arr)
    print(range)
else:
    print("Range cannot be determined")