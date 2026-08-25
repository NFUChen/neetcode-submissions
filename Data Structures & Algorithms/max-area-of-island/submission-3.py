class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = {}
        def dfs(key, r, c):
            if r < 0 or c < 0 or c > cols - 1 or r > rows - 1:
                return

            if grid[r][c] == 0:
                return
            
            grid[r][c] = 0

            if key not in count:
                count[key] = 0
            count[key] += 1

            dfs(key, r + 1, c)
            dfs(key, r - 1, c)
            dfs(key, r, c + 1)
            dfs(key, r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                
                dfs(f"{r}{c}", r, c)
        if len(count) == 0:
            return 0
        return max(count.values())
