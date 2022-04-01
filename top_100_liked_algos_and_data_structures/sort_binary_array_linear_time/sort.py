def sort(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[k] = 0
            k+=1
        
    for i in range(k, len(arr)):
        arr[i] = 1

    return arr

print(sort([1, 0, 1, 1,1, 0, 0, 0, 0, 1, 1, 0, 1, 0]))