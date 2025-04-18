"""
Given two strings s and t, return true if t is an of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list, t_list = {}, {}

        for i in range(len(s)):
            s_list[s[i]] = 1 + s_list.get(s[i], 0)
            t_list[t[i]] = 1 + t_list.get(t[i], 0)
        return s_list == t_list
