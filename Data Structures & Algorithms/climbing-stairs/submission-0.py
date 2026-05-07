class Solution:
    def climbStairs(self, n: int) -> int:
        #can elminate the entire cahce array because it
        #only uses the last two in the array each time

        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one