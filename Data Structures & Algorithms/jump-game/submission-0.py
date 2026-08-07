class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
       #work backwards, set a goal
       #if the previous goal can have a chain
       #to reach the newest goal and u can reach that
       #its good

    #set goal equal to the last thing in the array
        goal = len(nums) - 1

        #start stop step

        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= goal:
                goal = i
            
        
        return goal == 0