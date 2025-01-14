"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1  # Start from the last digit of both strings

        while i >= 0 or j >= 0 or carry:
            sum_ = carry  # Start with the carry from the previous step

            if i >= 0:  # Add bit from 'a' if available
                sum_ += int(a[i])
                i -= 1

            if j >= 0:  # Add bit from 'b' if available
                sum_ += int(b[j])
                j -= 1

            result = str(sum_ % 2) + result  # Append the current bit (0 or 1)
            carry = sum_ // 2  # Compute the carry (1 if sum_ is 2 or 3)

        return result
