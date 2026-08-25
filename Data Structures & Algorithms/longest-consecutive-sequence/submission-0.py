class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for num in num_set:
            # check if a num is a starter of the consecutive sequecne
            if (num - 1) not in num_set:
                curr_len = 0
                while (num + curr_len) in num_set:
                    curr_len += 1
                max_len = max(max_len, curr_len)

        return max_len
