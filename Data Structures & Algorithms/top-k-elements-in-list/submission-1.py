class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count to occurences of each value
        count = defaultdict(int) 

        #special array thats the same size as the input array
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] +=1
        for num, c in count.items():
            freq[c].append(num)
        
        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res