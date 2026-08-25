class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        count_map = {}
        for right in range(len(s)):
            char = s[right]
            count_map[char] = 1 + count_map.get(char, 0)
            while (right - left + 1) - max(count_map.values()) > k:
                count_map[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        
        return max_len

