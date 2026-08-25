class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while ( left < right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # search left
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # search right
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 if nums[right] != target else right




        # [3, 4, 5, 6, 1, 2]; target 1
        #. l        m     r
