"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
"""

class Solution:
    def searchInsert(self, nums, target):
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2  # Find the middle index

            if nums[mid] == target:  # If target is found, return its index
                return mid
            elif nums[mid] < target:  # If target is greater, search in the right half
                left = mid + 1
            else:  # If target is smaller, search in the left half
                right = mid - 1

        # If the target is not found, return the insertion position
        return left

