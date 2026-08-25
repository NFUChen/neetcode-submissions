class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1) ]
        dp[0] = True

        for end in range(len(s) + 1):
            for start in range(end):
                word = s[start:end]
                if dp[start] and word in wordDict:
                    dp[end] = True
        
        return dp[-1]
