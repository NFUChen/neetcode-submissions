class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        left = 0
        
        res =[]
        while (left < len(s) - 1):
            right = left
            while (s[right] != "#"):
                right += 1
            word_len = int(s[left:right])
            curr_word = s[right + 1: right + 1 + word_len]
            res.append(curr_word)
            left = right + 1 + word_len
        
        return res