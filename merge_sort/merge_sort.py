def mergesort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        mergesort(left)
        mergesort(right)

        a, b, c = 0, 0, 0
        
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1

    return list

list = [3, 4, 4, 6, 3352, 345, 56, 234, 5462, 456]
print(mergesort(list))