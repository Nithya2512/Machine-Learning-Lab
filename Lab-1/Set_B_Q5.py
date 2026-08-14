import random
def median(A):
    A.sort()
    n = len(A)
    if n % 2 == 0:
        mediann = (A[(n // 2) - 1] + A[n // 2]) / 2
    else:
        mediann = A[n // 2]
    return mediann
def mean(A):
    meann = sum(A) / len(A)
    return meann
def mode(A):
    B = set(A)
    max_count = 0
    mode_value = None
    for i in B:
        current_count = A.count(i)
        if current_count > max_count:
            max_count = current_count
            mode_value = i
    return mode_value

A = [random.randrange(100, 150) for i in range(100)]
rmean = mean(A)
rmedian = median(A)
rmode = mode(A)
print("Mean:", rmean)
print("Median:", rmedian)
print("Mode:", rmode)