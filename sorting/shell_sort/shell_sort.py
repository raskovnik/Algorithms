def shellsort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j - distance
            
            list[j] = temp
        distance = distance // 2

    return list

list = [26, 17, 20, 11, 23, 21, 13 ,18 ,24 ,4 ,14, 12, 22, 16, 15, 9, 25]
print(shellsort(list))