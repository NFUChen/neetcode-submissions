class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        rows, cols = len(grid), len(grid[0])


        def dfs(grid, r, c):
            if r < 0 or c < 0:
                return 0
            if r > rows -1 or c > cols -1:
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            
            area = 1
            area += dfs(grid, r + 1, c)
            area += dfs(grid, r - 1, c)
            area += dfs(grid, r, c + 1)
            area += dfs(grid, r, c - 1)
            return area
            
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                max_area = max(max_area ,dfs(grid, r, c))
        
        return max_area
                
