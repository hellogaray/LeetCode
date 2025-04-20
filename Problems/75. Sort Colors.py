def bucket_sort(nums):
    # Find the maximum value in the array
    max_val = max(nums)

    # Create a count array to store the counts of each distinct value
    counts = [0] * (max_val + 1)

    # Count the quantity of each value in the array
    for n in nums:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            nums[i] = n  # Fill the original array with the sorted values
            i += 1
    return nums

nums = [2,0,2,1,1,0]
print(bucket_sort(nums))