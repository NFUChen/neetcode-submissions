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
        right = 0
        while (right < len(s) - 1):
            peek = right
            while (s[peek] != "#"):
                peek += 1
            word_len = int(s[right:peek])
            word = s[peek + 1: peek + 1 + word_len]
            res.append(word)
            right = peek + 1 + word_len
        return res

