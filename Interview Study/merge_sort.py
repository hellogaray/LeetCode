def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublist
    Conquer: Recursively sort the sublist created in previous step
    Combine: Merge the sorted sublist created in previous step
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublist
    Return two sublist - left and right
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merge list
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else: # if left[i] >= right[j]
            l.append(right[j])
            j += 1


    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)
    if n <= 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54, 26, 62, 93, 77, 31, 44, 20, 55]
print("Unsorted List        : %s" % alist)
print("New Sorted List      : %s" % merge_sort(alist))
print("Is the list sorted?  : %s" % verify_sorted(merge_sort(alist)))