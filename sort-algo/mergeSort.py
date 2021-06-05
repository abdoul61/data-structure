# the merge sort techniquee uses the divide a conker
# first you consecutively divide the value the array by two untill the you have a subsets of one member
# then you compare each menber with and make the swapp
# The time complexity of merge sort algorthim is O(nlogn)


def mergeSort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    i = left
    j = mid + 1
    k = left
    B = [0]*(right + 1)
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]
            j = j + 1
        k = k + 1
    while i <= mid:
        B[k] = A[i]
        i = i + 1
        k = k + 1
    while j <= right:
        B[k] = A[j]
        j = j + 1
        k = k + 1
    for x in range(left, right + 1):
        A[x] = B[x]


A = [90, 65, 34, 11, 43, 45, 1, 5, 2]

print('the value of orginal array:', A)
mergeSort(A, 0, len(A)-1)
print('The value of sorted array', A)
