class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        stack = []
        def dfs(idx):
            if idx > len(nums) - 1:
                res.append(stack.copy())
                return
            
            stack.append(nums[idx])
            dfs(idx + 1)
            stack.pop()


            dfs(idx + 1)
        
        dfs(0)

        return res
