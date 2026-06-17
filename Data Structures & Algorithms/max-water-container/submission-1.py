class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxOut = 0
        while left <right:
            comp = min(heights[left],heights[right])
            out = (right - left) * comp
            maxOut = max(out,maxOut)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        return maxOut
            