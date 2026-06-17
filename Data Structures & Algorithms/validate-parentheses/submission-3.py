class Solution:
    def isValid(self, s: str) -> bool:
        checker = {"}":"{", ")":"(", "]":"["}
        stack = []
        for char in s:
            if char in checker:
                if stack and stack[-1] == checker[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False