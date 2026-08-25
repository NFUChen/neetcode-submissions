class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)):
            first = nums[idx]
            if first > 0:
                break
            if idx > 0 and first == nums[idx - 1]:
                continue

            
            left = idx + 1
            right = len(nums) - 1
            while (left < right):
                _3sum = nums[left] + nums[right] + first            
                if _3sum < 0:
                    left += 1
                elif _3sum > 0:
                    right -= 1
                else:
                    res.append(
                        [first, nums[left], nums[right]]
                    )
                    right -= 1
                    left += 1
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1   
        return res
