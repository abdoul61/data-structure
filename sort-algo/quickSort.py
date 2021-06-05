# This a quick sort technic algorithm who use a divider and concer algorithm
# the key point in this algo is find the pivot and then sort reccursively all the elemnt on is left and all the element on his right
# The pivot is found by usimg another function ** partition** in this particulary case
# The time complexity of the quick sort is O(nlog(n)) in the best case scenario which ais when the element are not alreasy sorted
def quickSort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quickSort(A, low, pi-1)
        quickSort(A, pi + 1, high)


def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <= j and A[j] > pivot:
            j = j - 1
        if i <= j:
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j


A = [90, 65, 34, 11, 43, 45, 1, 5, 2]

print('the value of orginal array:', A)
quickSort(A, 0, len(A)-1)
print('The value of sorted array', A)
