"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different. The test cases are generated such that the number of
unique combinations that sum up to target is less than 150 combinations for the given input.

Example:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Initialize a list to store the result combinations
        result = []

        def backtrack(index, current_combination, current_sum):
            # If the current combination sums up to the target, add it to the result
            if current_sum == target:
                result.append(current_combination.copy())
                return

            # If we've reached the end of candidates or exceeded the target sum, stop exploring
            if index >= len(candidates) or current_sum > target:
                return

            # Include the current candidate in the combination and explore further
            current_combination.append(candidates[index])
            backtrack(index, current_combination, current_sum + candidates[index])

            # Exclude the current candidate from the combination and explore the next candidate
            current_combination.pop()
            backtrack(index + 1, current_combination, current_sum)

        # Start the backtracking process from the beginning of the candidates list
        backtrack(0, [], 0)

        # Return the list of result combinations
        return result
