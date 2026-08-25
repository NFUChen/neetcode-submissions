class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(grid, r, c, visited):
            # three cases
            # out of bound
            # get blocked
            # visited        

            if r < 0 or c < 0:
                return 0
            if r > ROWS - 1 or c > COLS - 1:
                return 0
            if grid[r][c] == 1:
                return 0
            
            if (r, c) in visited:
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            count = 0
            visited.add( (r, c) )
            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r, c - 1, visited)

            visited.remove( (r, c) )
            return count
        
        return dfs(grid, 0, 0, visited)


        
        

