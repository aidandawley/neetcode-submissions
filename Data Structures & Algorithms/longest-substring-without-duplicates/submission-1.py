class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxRes = 0
        seen = set()


        for index in range(len(s)):

            while s[index] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            maxRes = max(maxRes, right - left)
        return maxRes
            
