class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for num in nums:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        
        return max_sum