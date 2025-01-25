"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
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

