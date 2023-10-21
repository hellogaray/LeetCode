"""
Given an array of positive integers arr, return the sum of all possible odd-length
sub-arrays of arr. A subarray is a contiguous subsequence of the array.

Example:
    Input: arr = [1,4,2,5,3]
    Output: 58
    Explanation: The odd-length sub-arrays of arr and their sums are:
    [1] = 1
    [4] = 4
    [2] = 2
    [5] = 5
    [3] = 3
    [1,4,2] = 7
    [4,2,5] = 11
    [2,5,3] = 10
    [1,4,2,5,3] = 15
    If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
"""

def sumOddLengthSubarrays(arr):
    result = 0
    n = len(arr)

    # Outer loop: starting index of subarray
    for start in range(n):
        # Inner loop: ending index of subarray, iterating by 2 to maintain odd length
        for end in range(start, n, 2):
            # Sum the elements in the current subarray and add to the result
            result += sum(arr[start:end + 1])

    return result
