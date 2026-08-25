class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        path = []
        res = []
        def dfs(idx):
            if idx > len(nums) - 1:
                res.append(path.copy())
                return
            

            path.append(nums[idx])
            dfs(idx + 1)
            path.pop()
            
            while (idx + 1 < len(nums) and nums[idx] == nums[idx + 1]):
                idx += 1
            dfs(idx + 1)
        
        dfs(0)

        return res