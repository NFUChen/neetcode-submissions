class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [3,6,7,11], h = 8
        # from 1 to 11
        def can_eat_up(piles: List[int], speed: int, h: int) -> bool:
            res = 0
            for p in piles:
                res += math.ceil(p / speed)
            
            return res <= h
        


        left = 1
        right = max(piles)
        min_hours = right

        while (left <= right):
            mid = (left + right) // 2
            if can_eat_up(piles, mid, h):
                right = mid - 1
                min_hours = min(min_hours, mid)
            else:
                left = mid + 1
            



        return min_hours
            