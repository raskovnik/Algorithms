def rotated_list(list) -> int:
    return list.index(min(list))

list = [5, 6, 9, 0, 1, 3, 4]

print(rotated_list(list))

list = [0, 1, 3, 4, 5, 6, 9]

def rotate_list(list, rotations):
    r_list = []
    for i in list[rotations + 1:]:
        r_list.append(i)
    for i in list[:rotations + 1]:
        r_list.append(i)
    
    print(r_list)

rotate_list(list, 3)
