class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, number in enumerate(nums):
            if target-number in indices:
                return [indices[target-number], index]
            indices[number] = index