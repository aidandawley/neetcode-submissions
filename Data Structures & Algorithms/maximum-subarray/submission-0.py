class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        currSum = 0
        for num in nums:
            currSum += num
            res = max (res, currSum)
            if currSum <= 0:
                currSum = 0
        return res