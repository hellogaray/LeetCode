"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the
type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
The ith item is said to match the rule if one of the following is true:
    ruleKey == "type" and ruleValue == typei.
    ruleKey == "color" and ruleValue == colori.
    ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

Example:
    Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
    ruleKey = "color", ruleValue = "silver"
    Output: 1
    Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
"""
class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        # Define a dictionary to map ruleKey to its corresponding index in the items list
        # "type" maps to index 0, "color" maps to index 1, "name" maps to index 2
        marker = {"type": 0, "color": 1, "name": 2}[ruleKey]

        # Initialize a counter for the number of items that match the rule
        score = sum(1 for item in items if item[marker] == ruleValue)

        # Return the count of items that match the rule
        return score
