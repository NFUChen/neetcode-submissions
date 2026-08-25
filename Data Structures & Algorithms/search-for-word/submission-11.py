class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r, c, idx):
            if r < 0 or c < 0:
                return
            
            if r > rows - 1 or c > cols - 1:
                return
                
            if (r, c) in visited:
                return
                
            if word[idx] != board[r][c]:
                return
            
            visited.add( (r, c) )
            if idx == len(word) - 1:
                print(visited)
                nonlocal found
                found = True
                return
            dfs(r + 1, c, idx + 1)
            dfs(r - 1, c, idx + 1)
            dfs(r, c + 1, idx + 1)
            dfs(r, c - 1, idx + 1)
            visited.remove( (r, c) )            
        
        for r in range(rows):
            for c in range(cols):
                if word[0] != board[r][c]:
                    continue
                if found:
                    return True
                dfs(r, c, 0)
        


        return found
        