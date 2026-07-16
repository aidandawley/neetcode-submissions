class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        countNeeded = {}
        #init the checker for needed string
        for char in t:
            countNeeded[char] = 1 + countNeeded.get(char,0)
        
        have = 0
        need = len(countNeeded)

        res = [-1, -1]
        resLen = float("infinity")

        l = 0
        #what we have, need to compare this too the checker constantly
        countCurrent = {}
        for r in range(len(s)):
            char = s[r]
            countCurrent[char] = 1 + countCurrent.get(char, 0)

            if (char in countNeeded) and (countCurrent[char] == countNeeded[char]):
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                countCurrent[s[l]] -=1
                if s[l] in countNeeded and countCurrent[s[l]] < countNeeded[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

        


        
