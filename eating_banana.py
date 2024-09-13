class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low < high:
            mid = (low + high) // 2
            rh = 0  
            
            
            for i in range(len(piles)):
                rh += math.ceil(piles[i] / mid)
            
           
            if rh > h:
                low = mid + 1
            else:
                high = mid  
                
        return low
