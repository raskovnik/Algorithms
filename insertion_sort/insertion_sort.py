def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        value_to_sort = sequence[i]

        while sequence[i-1] > value_to_sort and i > 0:
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            i = i - 1

    return sequence

print(insertion_sort([5,6,5,1,5,7,8,1,2,4,6,7,8,9,0]))