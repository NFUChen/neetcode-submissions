class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                tri = [
                    nums[i], nums[left], nums[right]
                ]
                _3sum = sum(tri)
                if _3sum == 0:
                    res.append(tri)
                    left += 1
                    right -=1
                    # checking the left duplicates
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                else:
                    if _3sum < 0:
                        left += 1
                    elif _3sum > 0:
                        right -= 1

        return res
                