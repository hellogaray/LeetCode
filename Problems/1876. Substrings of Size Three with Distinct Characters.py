"""
A string is good if there are no repeated characters.
Given a string s, return the number of good substrings of length three in s.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

Example:
    Input: s = "xyzzaz"
    Output: 1
    Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
    The only good substring of length 3 is "xyz".
"""
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize a variable to store the count of good substrings
        results = 0

        # Iterate through the string, considering substrings of length 3
        for i in range(len(s) - 2):
            # Extract a substring of length 3
            substring = s[i:i + 3]

            # Check if all characters in the substring are distinct
            if len(set(substring)) == 3:
                # If yes, increment the count of good substrings
                results += 1

        # Return the total count of good substrings
        return results
