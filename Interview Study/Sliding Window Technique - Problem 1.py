# Easy: Find Maximum Sum of a Subarray of Fixed Size (K)
# Problem: Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

# Example:
# Input: nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: The subarray `[5, 1, 3]` has the maximum sum of 9.

def max_sum(array, window_size):
    if len(array) < window_size:
        return None

    window_sum = sum(array[:window_size])
    max_sum = window_sum

    for i in range(len(array) - window_size):
        window_sum = window_sum - array[i] + array[i + window_size]
        max_sum = max(max_sum, window_sum)
    return max_sum


# Test Case:
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum(nums, k))

nums = [2, 1]
k = 3
print(max_sum(nums, k))

nums = [2, 1, 5]
k = 3
print(max_sum(nums, k))