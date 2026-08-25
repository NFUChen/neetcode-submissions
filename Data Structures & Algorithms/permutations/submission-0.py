class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        used = [False for _ in range(len(nums))]
        res = []

        def dfs(idx):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            
            

            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                dfs(i + 1)

                path.pop()
                used[i] = False

            
        
        dfs(0)
        return res