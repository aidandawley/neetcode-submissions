class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # [3,4,5,6,1,2] <- if middle is greater than there is no min
        # [6,7,1,2,3,4,5] <- if the right side is great than mid 
        # then it had the min
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid
            
        return nums[left]