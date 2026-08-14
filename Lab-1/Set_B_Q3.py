def common(lst1,lst2):
    count=0
    for i in lst1:
        if i in lst2:
            count+=1
            lst2.remove(i)
    return count
n1=int(input("Number of elements in list A:"))
A=[input() for i in range(n1)]
n2=int(input("Number of elements in list B:"))
B=[input() for i in range(n2)]
count=common(A,B)
print(count)