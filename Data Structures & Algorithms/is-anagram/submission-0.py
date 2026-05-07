class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first=0
        last=0

        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            #.get allows us to make sure there isnt an error
            # dict.get(has insert, starting value)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

