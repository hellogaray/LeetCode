# Hard: Longest Subarray with Sum at Most K
# Problem: Given an array nums and an integer k, find the length of the longest
# contiguous subarray where the sum does not exceed k.

# Example:
# nums = [3, 1, 2, 5, 1, 1, 1, 4], k = 7
# Output: 4
# Explanation: The longest valid subarray is `[2, 5, 1, 1]` with a sum of 7.



def max_sum_subarray(s, t):
    left = 0
    seen = set()
    smallest = len(s)

    if len(s) < len(t):
        return ""

    for right in range(len(s)):
        while t in s[left:right]:
            left =+ 1
            print(s[left:right])
        else:
            right =+ 1
            print(s[left:right])


    print(seen)
    return smallest

s = "ADOBECODEBANC"
t = "ABC"
output = "BANC"
print("here:")
print(t in s)

print(output == max_sum_subarray(s, t))


s = "a"
t = "a"
output = "a"
print(output == max_sum_subarray(s, t))


s = "a"
t = "aa"
output = ""
print(output == max_sum_subarray(s, t))

