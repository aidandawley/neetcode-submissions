class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add to hasmap
        #if num-1 exists start tracing back
        #if num-1 doesnt exist we hit the start of the array
        #if num + 1 exists we go up?
        res = 0
        seen = set()
        for index in range(len(nums)):
            number = nums[index]
            localRes = 0
            seen.add(number)
            while number+1 in seen:
                number +=1 
            while number-1 in seen:
                number-=1
                localRes+=1
            res = max(res, localRes+1)
        return res
            



