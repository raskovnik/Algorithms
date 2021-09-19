def brute_force(list, target):
    for i in list:
        for j in list[1::]:
            if i + j == target:
                return i, j

print(brute_force([1, 2, 2, 3, 4, 5, 5, 6], 3))