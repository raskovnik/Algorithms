def find_max(arr):
    n = len(arr)
    if n < 2: return 

    arr.sort()
    if (arr[0] * arr[1]) > (arr[n - 1] * arr[n - 2]):
        print(f"The pair is {arr[0]} and {arr[1]}")
    else:
        print(f"The pair is {arr[n - 1]} and {arr[n - 2]}")

find_max([-10, -3, 5, 6, -20])