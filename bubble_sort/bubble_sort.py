def bubble_sort(sequence):
    indexing_length = len(sequence) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(indexing_length):
            if sequence[i] > sequence[i+1]:
                sorted = False
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]

    return sequence

print(bubble_sort([5,6,5,1,5,7,8,1,2,4,6,7,8,9,0]))