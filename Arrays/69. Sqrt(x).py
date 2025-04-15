"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.
"""


lass Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        start, end, answer = 0, (x//2) , 0
        while start <= end:
            mid = ((start + end) // 2)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                answer = mid
                start = mid + 1
            else:
                end = mid - 1
        return answer