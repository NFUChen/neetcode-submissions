class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add close_n if close < open_n
        # add open_n if open_n < n
        
        res = []
        parans = []
        def dfs(open, close):
            if open == close == n:
                res.append(
                    "".join(parans)
                )
                return
            if open < n:
                parans.append("(")
                dfs(open + 1, close)
                parans.pop()
            if close < open:
                parans.append(")")
                dfs(open, close + 1)
                parans.pop()

        dfs(0, 0)
        return res