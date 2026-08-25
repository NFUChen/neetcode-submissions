class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []
        for char in s:
            if char in lookup:
                stack.append(lookup[char])
            else:
                if len(stack) == 0:
                    return False
                if char != stack.pop():
                    return False
        
        return len(stack) == 0

            

