def linear_search(list, target):
    for index, item in enumerate(list):
       if item == target:
           return index
    return None



slist = [1,0,3,4,50,3,2,9,23,124]
target = 9
print(linear_search(slist, target))