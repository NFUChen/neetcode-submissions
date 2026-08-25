class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while (idx < len(s)):
            len_seeker = idx
            while (s[len_seeker] != "#"):
                len_seeker += 1 
            # len_seeker == "#"
            curr_len = int(s[idx: len_seeker])
            word = s[len_seeker + 1: len_seeker + 1 +curr_len]
            res.append(word)

            idx = len_seeker + 1 +curr_len
        return res

        

            
        
        return res
