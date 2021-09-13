def selection_sort(sequence):
    for i in range(0, len(sequence) - 1):
        min_value = i
        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[min_value]:
                min_value = j
            
            if min_value != i:
                sequence[min_value], sequence[i] = sequence[i], sequence[min_value]
            
    return sequence

print(selection_sort([5,6,5,1,5,7,8,1,2,4,6,7,8,9,0]))
