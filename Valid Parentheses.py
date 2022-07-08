def isValid(s):
    stack = []
    hash = {')': '(', ']': '[', '}': '{'}
    for bracket in s:
        if bracket in hash:
            if stack and stack[-1] == hash[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    return True if not stack else False
