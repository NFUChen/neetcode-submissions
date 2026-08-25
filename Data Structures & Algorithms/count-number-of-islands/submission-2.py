from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counts = 0
        rows, cols = len(grid), len(grid[0])


        def dfs(grid, r, c):
            if r > rows - 1 or c > cols - 1:
                return
            if r < 0 or c < 0:
                return

            if grid[r][c] == "0":
                return

            
            grid[r][c] = "0"

            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    counts += 1
        

        return counts
                
    
