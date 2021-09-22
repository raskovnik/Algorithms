def missing_element(arr):
    n = len(arr)
    total = sum(arr)

    return (n + 1) + n *(n + 1) // 2 - total

print(f"The missing element is {missing_element([3, 2, 4, 6, 1])}")