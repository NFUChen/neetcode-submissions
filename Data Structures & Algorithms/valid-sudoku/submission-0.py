class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(len(board)):
            for c in range(len(board)):
                curr = board[r][c]
                if curr == ".":
                    continue
                _row_repr = f"{curr} in row: {r}"
                _col_repr = f"{curr} in col: {c}"
                _grid_repr = f"{curr} in grid: ({r//3},{c//3})"
                _reprs = [_row_repr, _col_repr, _grid_repr]
                for _repr in _reprs:
                    if _repr in seen:
                        return False
                    seen.add(_repr)
        return True