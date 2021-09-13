def binary_search(list, number):
    start, end = 0, len(list) - 1
    while start <= end:
        midpoint = start + (end - start) // 2
        if list[midpoint] == number:
            return midpoint
        else:
            if list[midpoint] <= number:
                start = midpoint + 1

            if list[midpoint] >= number:
                end = midpoint - 1
    
print(binary_search([0, 1, 1, 2, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9], 9))