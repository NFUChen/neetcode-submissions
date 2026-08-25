class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while (left < right):
                triple = [
                    nums[i], nums[left], nums[right]
                ]
                _sum = sum(triple)
                if _sum == 0:
                    res.append(triple)
                    while (left < right and nums[left] == nums[left  + 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right -= 1
                    left += 1
                    right -= 1
                else:
                    if _sum > 0:
                        right -= 1
                    else:
                        left += 1
        
        return res