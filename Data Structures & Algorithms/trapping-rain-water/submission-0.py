class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = []
        currMax = 0
        for item in height:
            leftMax.append(currMax)
            currMax = max(currMax, item)
        
        rightMax = []
        currMax = 0
        for item in reversed(height):
            rightMax.append(currMax)
            currMax = max(currMax, item)
        rightMax.reverse()
        res = 0
        for i in range(len(height)):
            water = min(leftMax[i], rightMax[i]) - height[i]
            res += max(0, water)
        return res