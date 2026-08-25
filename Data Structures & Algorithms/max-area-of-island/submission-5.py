class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_area = 0

        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            
            count_area = 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

            return count_area
            
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    island_area = dfs(i,j)
                    max_area = max(max_area, island_area)
        return max_area
