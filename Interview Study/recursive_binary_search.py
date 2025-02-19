def linear_search(list, target):

    if len(list) == 0:
        return False
    else:
        mid = (len(list) // 2)
        if list[mid] == target:
            return mid
        else:
            if list[mid] < target:
                return linear_search(list[mid + 1:], target)
            else:
                return linear_search(list[:mid], target)


slist = [1,2,3,4,5,6,7,8,9]
target = 1
print(linear_search(slist, target))