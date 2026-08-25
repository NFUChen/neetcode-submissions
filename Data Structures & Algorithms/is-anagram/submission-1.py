class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_count = dict()
        t_char_count = dict()
        for word in s:
            if word not in s_char_count:
                s_char_count[word] = 0
            s_char_count[word] += 1
        
        for word in t:
            if word not in t_char_count:
                t_char_count[word] = 0
            t_char_count[word] += 1
        

        return s_char_count == t_char_count
