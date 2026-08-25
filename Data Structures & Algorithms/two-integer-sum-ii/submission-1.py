class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while (left < right):
            _sum = nums[left] + nums[right]
            if _sum == target:
                return [left + 1, right + 1]
            
            if _sum > target:
                right -= 1
            
            if _sum < target:
                left += 1
