def runningSum(nums):
    completed = []
    for i, value in enumerate(nums):
        if i == 0:
            completed.append(value)
        else:
            completed.append(value + completed[i - 1])
    return completed
