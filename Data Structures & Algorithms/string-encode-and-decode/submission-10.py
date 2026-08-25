class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        
        return res



    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        while (left < len(s)):
            seeker = left
            while (s[seeker] != "#"):
                seeker += 1
            
            word_len = int(s[left:seeker])
            word_start = seeker + 1
            word_end = word_start + word_len
            res.append(s[word_start: word_end])

            left = word_end
        
        return res