class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(grid, r, c, visited):
            ROWS = len(grid)
            COLS = len(grid[0])
            # three cases
                # 1. out of bound (< 0 or > dimension)
                # 2. get blocked grid[r][c] == 1
                # 3. already vsisted 
            if min(r, c) < 0 or (r == ROWS or c == COLS):
                return 0
            if grid[r][c] == 1:
                return 0
            
            if (r, c) in visited:
                return 0

            # successful case
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visited.add((r, c))
            count = 0
            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r, c - 1, visited)

            visited.remove((r, c) )
            return count
        
        return dfs(grid, 0, 0, visited)

        
        

