class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1) ]
        dp[0] = True
        word_set = set(wordDict)

        for end in range(len(s) + 1):
            for start in range(end):
                word = s[start:end]
                if dp[start] and word in word_set:
                    print(word)
                    dp[end] = True
        
        print(dp)

        return dp[-1]