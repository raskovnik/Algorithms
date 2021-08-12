def merge_sort(sequence):
    merging(sequence, 0, len(sequence) - 1)

def merging(sequence, first, last):
    if first < last:
        middle = (first + last) // 2
        merging(sequence, first, middle)
        merging(sequence, middle + 1, last)
        merge(sequence, first, middle, last)

def merge(sequence, first, middle, last):
    left_half = sequence[first:middle]
    right_half = sequence[middle:last + 1]
    right_half.append(9999999)
    left_half.append(9999999)
    i = j = 0
    for k in range(first, last + 1):
        if left_half[i] <= right_half[i]:
            sequence[k] = left_half[i]
            i += 1

        else:
            sequence[k] = right_half[j]
            j += 1

    return sequence

print(merge_sort([5,6,5,1,5,7,8,1,2,4,6,7,8,9,0]))
        
