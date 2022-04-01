a = [3, 5, 6, 2, 4, 6, 7, 2, 5,7, 3, 2,7]
a.sort()

def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1

        elif arr[mid] < target: right = mid - 1
        else: left = mid + 1

    return result

def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1

        elif arr[mid] == target: right = mid - 1
        else: left = mid + 1