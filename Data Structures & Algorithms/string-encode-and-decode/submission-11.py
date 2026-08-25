class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for char in strs:
            res += f"{len(char)}#{char}"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while (i < len(s)):
            seeker = i
            while (s[seeker] != "#"):
                seeker += 1
            # till this point, seeker is #
            char_len = int(s[i:seeker])
            word = s[seeker + 1: seeker + 1 + char_len]
            res.append(word)
            i = seeker + 1 + char_len
        
        return res
