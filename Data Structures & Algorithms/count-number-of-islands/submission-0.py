from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(grid, r, c):
            if r < 0 or c < 0:
                return
            if r > rows - 1 or c > cols - 1:
                return
            if (grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            
            bfs(grid, r + 1, c)
            bfs(grid, r - 1, c)
            bfs(grid, r, c + 1)
            bfs(grid, r, c - 1)



        islands = 0
        

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1"):
                    bfs(grid,r, c)
                    islands += 1
        
        return islands



    
