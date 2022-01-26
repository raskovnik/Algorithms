def linear_search(list, item):
    index = 0
    found = False
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1
    return found

def linear_search2(list, item):
    for i in list:
        if i == item:
            return True
    return False

def linear_search3(list, target):
    list.sort()
    for i in list:
        if i == target: return True, time.now() - start
        if i > target: return False, time.now() - start
    

list = [1, 3, 5, 3, 5,6, 5, 7, 3, 3,55435,6]

print(linear_search(list, 5))
print(linear_search2(list, 5))
print(linear_search3(list, 4))