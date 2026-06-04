class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for i in range(len(nums)):
            
            if nums[i] - 1 not in seen:
                currRes = 1
                number = nums[i]
                while number + 1 in seen:
                    currRes +=1
                    number +=1
                
                res = max(res, currRes)
        return res