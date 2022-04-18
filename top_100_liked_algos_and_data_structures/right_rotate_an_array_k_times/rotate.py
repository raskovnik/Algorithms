def rotate(arr, k):
    return arr[len(arr) - k: len(arr)] + (arr[0: len(arr) - k])

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))