class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(",
                    "}": "{",
                    "]": "["}
        openStack = []
        for c in s:
            if c in brackets:
                if openStack and openStack[-1] == brackets[c]:
                    openStack.pop()
                else:
                    return False
            else:
                openStack.append(c)
        return True if not openStack else False
