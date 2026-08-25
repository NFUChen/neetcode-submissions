class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        def can_eat_up(speed: int):
            eat_up_hour = 0
            for p in piles:
                eat_up_hour +=  math.ceil(p / speed)
            
            return eat_up_hour <= h

        while (left < right):
            mid = (left + right) // 2

            if can_eat_up(mid):
                res = min(res, mid)
                right = mid
            else:
                left = mid + 1
        
        return res
        
        
            
