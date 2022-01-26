def out_in_place(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence[0]
        return out_in_place([x for x in sequence[1:] if x < pivot]) + \
                [pivot] + \
                out_in_place([x for x in sequence[1:] if x  >= pivot ])

print(out_in_place([5,6,5,1,5,7,8,1,2,4,6,7,8,9,0]))