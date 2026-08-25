class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
            anagram_map[sorted_word].append(word)
        
        res = [val for val in anagram_map.values()]

        return res