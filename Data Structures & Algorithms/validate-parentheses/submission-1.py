class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            "(": ")", "[": "]", "{": "}"
        }
        stack = []
        for paran in s:
            if paran in lookup:
                stack.append(lookup[paran])
            else:
                if len(stack) == 0:
                    return False
                if paran != stack.pop():
                    return False
        

        return len(stack) == 0