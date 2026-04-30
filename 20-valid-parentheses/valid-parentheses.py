class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != matching[char]:
                    return False
                stack.pop()
        return stack == []