class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        left = defaultdict(int)
        right = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            left[s[i]] +=1
            right[t[i]] +=1
        
        if left == right:
            return True
        else:
            return False
