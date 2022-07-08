def longestCommonPrefix(strs):
    prefix = ""
    for position, letters in enumerate(strs[0]):
        for words in strs[1:]:
            if len(words) < position + 1 or words[position] != letters:
                return prefix
        else:
            prefix += letters
    return prefix
