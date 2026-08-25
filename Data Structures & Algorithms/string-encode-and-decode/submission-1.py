class Solution:
    def encode(self, strs: List[str]) -> str:
        # ["neet","code","love","you"]
        # 4#neet4#code
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        while (left < len(s)):
            peek = left
            while (s[peek] != "#"):
                peek += 1
            word_len = int(s[left:peek])
            word = s[peek + 1: peek+ 1 + word_len]
            res.append(word)
            left = peek + 1 + word_len
        return res