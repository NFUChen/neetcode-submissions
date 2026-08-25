class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        


        def kadane(nums: List[int]):
            curr_sum = 0
            max_sum = nums[0]

            for num in nums:
                if curr_sum < 0:
                    curr_sum = 0
                curr_sum += num

                max_sum = max(max_sum, curr_sum)
            
            return max_sum

        def inverted_kadane(nums: List[int]):
            curr_sum = 0
            min_sum = nums[0]
            for num in nums:
                if curr_sum > 0:
                    curr_sum = 0
                curr_sum += num

                min_sum = min(min_sum, curr_sum)
            return min_sum

        total = sum(nums)
        max_kadane = kadane(nums)
        min_kadane = inverted_kadane(nums)

        if max_kadane < 0:
            return max_kadane
        
        return max(total - min_kadane, max_kadane)
