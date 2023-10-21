"""
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.

Example:
    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
"""
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Convert the allowed characters to a set for efficient membership testing
        allowed_set = set(allowed)

        # Initialize the count with the total number of words
        count = len(words)

        # Iterate through each word in the list
        for word in words:
            # Check each character in the word
            for char in word:
                # If a character is not in the allowed set, decrement the count and break
                if char not in allowed_set:
                    count -= 1
                    break

        # Return the final count of consistent strings
        return count
