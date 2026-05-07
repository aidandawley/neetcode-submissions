class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #lets make a hash map
        #lets check if the target minus index exists in the map

        seen = {}
        for i, x in enumerate(nums):
            
            comp = target - x
            if comp in seen:
                return [seen[comp], i]
            seen[x] = i