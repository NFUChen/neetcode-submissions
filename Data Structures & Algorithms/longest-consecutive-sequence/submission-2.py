class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for num in num_set:
            curr_len = 0
            check_num = num
            while (check_num in num_set):
                curr_len += 1
                check_num += 1
            max_len = max(max_len, curr_len)
        
        return max_len