class Solution:
    def isPalindrome(self, s: str) -> bool:
        target_chars = [
            char.lower() for char in s if char.isalnum()
        ]
        left = 0
        right = len(target_chars) - 1
        while (left < right):
            if target_chars[left] != target_chars[right]:
                return False
            left += 1
            right -= 1
        
        return True