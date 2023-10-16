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
        unique_chars = set()
        max_length = 0
        left_boundary = 0
        for right_boundary in range(len(s)):
            while s[right_boundary] in unique_chars:
                unique_chars.remove(s[left_boundary])
                left_boundary += 1
            unique_chars.add(s[right_boundary])
            current_length = right_boundary - left_boundary + 1
            max_length = max(max_length,current_length )
        return max_length
