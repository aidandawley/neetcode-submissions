class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #thinking has tabel rn
        #hash wiith key:number value:frequency
        
        #we are going to keep a seperate hash for frequency
        #indexes: actual counts of element, value: actual value
        value_tracker= {}
        #create buckets
        #we are using buckets because we want an array of size nums
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            value_tracker[num] = 1 + value_tracker.get(num, 0)
        for value in value_tracker:
            freq[value_tracker[value]].append(value)
        
        #now how to display?
        #going to define an array to return

        solution = []

        #start at end, go till 0, decriment by 1 each time
        for i in range (len(freq) -1 , 0, -1):
            for n in freq[i]:
                solution.append(n)
                if len(solution) == k:
                    return solution



        

            


        

