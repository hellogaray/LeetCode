def binary_search(list, target):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = ((start + end) // 2)
        if list[mid] > target:
            end = mid - 1
        elif list[mid] < target:
            start = mid + 1
        else:
            return mid
    return None



slist = [1,2,3,4,5,6,7,8,9]
target = 2
print(binary_search(slist, target))