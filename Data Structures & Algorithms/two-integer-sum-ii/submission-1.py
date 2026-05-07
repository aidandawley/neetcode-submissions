class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #not allowed hash because of space
        #sorted!

        #we should probably use two pointers i and j
        #start at the front and back
        i=0
        j=len(numbers)-1
        while i < j:
            if(numbers[i]+numbers[j] < target):
                i+=1
            elif(numbers[i]+numbers[j] > target):
                j-=1
            else:
                return [i+1,j+1]


