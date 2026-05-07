class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        result = right
        while left <= right:
            middle = (right+left) //2

            speed = 0
            for element in piles:
                speed += math.ceil(element/middle)

            if speed <= h:
                result = middle
                right = middle - 1
            else:
                left = middle +1

        return result

            
