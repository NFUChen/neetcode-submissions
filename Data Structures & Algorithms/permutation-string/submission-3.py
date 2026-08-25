class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sorted_s1 = sorted(s1)
        first_k_of_s2 = s2[:len(s1)]
        if sorted(first_k_of_s2) == sorted_s1:
            return True
        
        for right in range(len(s1), len(s2) + 1):
            left = right - len(s1)
            window = sorted(s2[left:right])
            print(left, right,window)
            if window == sorted_s1:
                return True

        

        return False