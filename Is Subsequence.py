def isSubsequence(s, t):
    s_position, t_position = 0, 0
    while s_position < len(s) and t_position < len(t):
        if s[s_position] == t[t_position]:
            s_position += 1
        t_position += 1
    return True if s_position == len(s) else False
