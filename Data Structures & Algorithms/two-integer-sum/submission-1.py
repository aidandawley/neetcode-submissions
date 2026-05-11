class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i,x in enumerate(nums):
            calculation = target - x
            if calculation in seen:
                return [seen[calculation], i]
            seen[x] = i