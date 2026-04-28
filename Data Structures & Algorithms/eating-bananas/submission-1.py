import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high 

        while low <= high:
            mid = low + (high - low) // 2
            total_hrs = 0 
            for pile in piles:
                total_hrs += math.ceil(pile/mid)
            if total_hrs <= h:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res




        