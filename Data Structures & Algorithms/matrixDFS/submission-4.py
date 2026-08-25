class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def dfs(r, c):
            if min(r, c) < 0 or r > rows - 1 or c > cols - 1:
                return 0

            if  grid[r][c] == 1:
                return 0
            if (r, c) in visited:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1
            
            visited.add( (r, c) )
            count = 0
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            visited.remove( (r, c) )

            return count
        

        return dfs(0, 0)
            


        
        

