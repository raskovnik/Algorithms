def kth(arr, k):
    arr.sort()
    return arr[k - 1]

print(kth([7, 4, 6, 3, 9, 1], 3))