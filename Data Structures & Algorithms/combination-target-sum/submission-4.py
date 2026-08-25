class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, subset, total):
            if i > len(nums) - 1:
                return
            if total > target:
                return
            
            if total == target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i, subset, total + nums[i])
            subset.pop()
            dfs(i + 1, subset, total)
        

        dfs(0, [], 0)

        return res