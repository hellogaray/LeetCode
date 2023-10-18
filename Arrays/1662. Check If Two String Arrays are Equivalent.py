"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example:
    Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    Output: true
    Explanation:
        word1 represents string "ab" + "c" -> "abc"
        word2 represents string "a" + "bc" -> "abc"
        The strings are the same, so return true.
"""


class Solution(object):
    def arrayStringsAreEqual(self, words_list1, words_list2):
        """
        :type words_list1: List[str]
        :type words_list2: List[str]
        :rtype: bool
        """
        # Iterate through characters in both word lists simultaneously using zip
        for char1, char2 in zip(self.generate_chars(words_list1), self.generate_chars(words_list2)):
            # If characters are not equal, the two arrays of strings are not equal
            if char1 != char2:
                return False

        # If all characters are equal, the two arrays of strings are equal
        return True

    def generate_chars(self, words_list):
        # Generator function to yield characters from a list of words
        for word in words_list:
            for char in word:
                yield char
        # Add a None at the end to mark the end of characters
        yield None
