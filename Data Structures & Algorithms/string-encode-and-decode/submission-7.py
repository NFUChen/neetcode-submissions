class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        while (left <= len(s) - 1):
            seeker = left
            while (s[seeker] != "#"):
                seeker += 1
            
            # for now we got seeker at index of "#"
            curr_len = int(s[left:seeker])
            word_start = seeker + 1
            word = s[word_start: word_start + curr_len]
            res.append(word)

            left = word_start + curr_len
        
        return res


        
