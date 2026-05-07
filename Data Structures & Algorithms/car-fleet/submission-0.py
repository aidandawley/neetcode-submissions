class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = 1
        pairs = [(p,s) for p,s in zip (position, speed)]
        pairs.sort(reverse = True )
        
        prev_pos, prev_speed = pairs[0]
        prev_time = (target - prev_pos)/prev_speed
        for i in range (1, len(pairs)):
           curr_pos, curr_speed = pairs[i]
           curr_time = (target - curr_pos)/curr_speed

           if curr_time > prev_time:
            fleets +=1
            prev_time=curr_time
        return fleets





