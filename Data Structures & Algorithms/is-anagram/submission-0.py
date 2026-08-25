class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def _count(word: str) -> dict[str, int]:
            _map = {}
            for char in word:
                if char not in _map:
                    _map[char] = 0
                _map[char] += 1
            return _map

        s_count = _count(s)
        t_count = _count(t)
        return s_count == t_count

