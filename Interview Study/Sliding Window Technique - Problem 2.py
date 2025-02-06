# Medium: Longest Substring Without Repeating Characters
# Problem: Given a string s, find the length of the longest substring without repeating characters.

# Example:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with a length of 3.

def longest_substring(s):
    left = 0
    seen = set()
    longest = 0

    for right in range(len(s)):
        # If a duplicate is found, move left pointer
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])  # Add the new character to the set
        longest = max(longest, right - left + 1)  # Update max length

    return longest

s = "a"
solution = 1
print(solution == longest_substring(s))

s = "abcdef"
solution = 6
print(solution == longest_substring(s))

s = "aaaaaa"
solution = 1
print(solution == longest_substring(s))

s = "abcabcbb"
solution = 3  # "abc"
print(solution == longest_substring(s))

s = "pwwkew"
solution = 3  # "wke"
print(solution == longest_substring(s))

s = "123@123!"
solution = 5  # "123@!"
print(solution == longest_substring(s))

s = ""
solution = 0
print(solution == longest_substring(s))

s = "dv df"
solution = 4  # "v df"
print(solution == longest_substring(s))

s = "abcdeafghijklmno"
solution = 15  # "bcdeafghijklmno"
print(solution == longest_substring(s))

s = "a" * 10**5
solution = 1
print(solution == longest_substring(s))
