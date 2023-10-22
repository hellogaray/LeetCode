"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker
starts his trip on point 0 with altitude equal 0. You are given an integer array gain of length n where gain[i]
is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example:
    Input: gain = [-5,1,5,0,-7]
    Output: 1
    Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
"""
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Initialize the altitudes list with the starting altitude of 0
        altitudes = [0]

        # Iterate through the gain values to calculate altitudes at each point
        for gain_value in gain:
            # Append the new altitude, which is the sum of the gain and the previous altitude
            altitudes.append(gain_value + altitudes[-1])

        # Return the maximum altitude reached
        return max(altitudes)
