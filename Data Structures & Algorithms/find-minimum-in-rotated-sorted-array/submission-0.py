class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        res = float("inf")
        right = len(nums) - 1
        while (left <= right):
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
        return res
        # [3,4,5,6,1,2]
        #  0   m     5r -> mid = 2

        #      2l     5r
        #        3l.  5r
        #           4l 5r