def runningSum(sum):
    completed = []
    for i, value in enumerate(sum):
        if i == 0:
            completed.append(value)
        else:
            completed.append(value + completed[i - 1])
    return completed
