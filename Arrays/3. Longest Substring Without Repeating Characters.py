"""
Given a string s, find the length of the longest substring without repeating characters.

Example:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Set to keep track of unique characters in the current substring
        unique_chars = set()

        # Variable to store the length of the longest substring without repeating characters
        max_length = 0

        # Variable to represent the left boundary of the current substring
        left_boundary = 0

        # Iterate over the characters in the input string
        for right_boundary in range(len(s)):
            # Check if the current character is already in the unique_chars set
            while s[right_boundary] in unique_chars:
                # If yes, remove the character at the left boundary and move the left boundary to the right
                unique_chars.remove(s[left_boundary])
                left_boundary += 1

            # Add the unique character at the current right boundary to the set
            unique_chars.add(s[right_boundary])

            # Calculate the length of the current substring
            current_length = right_boundary - left_boundary + 1

            # Update max_length with the maximum length encountered so far
            max_length = max(max_length, current_length)

        # Return the length of the longest substring without repeating characters
        return max_length

