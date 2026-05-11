class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        left = {}
        right = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            left[s[i]] = 1 + left.get(s[i], 0)
            right[t[i]] = 1 + right.get(t[i], 0)
        
        if left == right:
            return True
        else:
            return False
