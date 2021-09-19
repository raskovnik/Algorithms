def find_pair(list, target):
    list.sort()
    (low, high) = (0, len(list) - 1)

    while low < high:
        if list[low] + list[high] == target:
            print("pair found", (list[low], list[high]))
            return

        if list[low] + list[high] < target:
            low = low + 1
        else:
            high = high - 1

    print("Pair not found")

