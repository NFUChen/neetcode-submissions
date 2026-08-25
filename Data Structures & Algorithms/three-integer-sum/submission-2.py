class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1
            while (left < right):
                _3 = [
                    nums[idx], nums[left], nums[right]
                ]
                _3sum = sum(_3)
                if _3sum == 0:
                    res.append(_3)
                    left += 1
                    right -= 1
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
                else:
                    if _3sum < 0:
                        left += 1
                    elif _3sum > 0:
                        right -= 1
        return res
                    
