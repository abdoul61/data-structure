# To perform this technique of sorting algorithm we first divide the length of all the
# the data by two then (n/2 = gap) then we start form first elemnt of then we comparing that elemnt with an element
# at gaps form him!, if greater then we perfom swapp . do not forgget to do it from both side of the element
# the time complexity of the shell sort is O(nlog(n)) in worst case and the best case is O(nlog(n))


def shellSort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        i = gap
        while i < n:
            temp = A[i]
            j = i - gap
            while j >= 0 and A[j] > temp:
                A[j + gap] = A[j]
                j = j - gap
            A[j + gap] = temp
            i = i + 1
        gap = gap // 2


A = [90, 34, 65, 34, 11, 43, 45, 1, 5, 2]

print('the value of orginal array:', A)
shellSort(A)
print('The value of sorted array', A)
