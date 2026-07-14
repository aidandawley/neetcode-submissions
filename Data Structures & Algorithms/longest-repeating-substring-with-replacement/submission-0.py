class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #size of window - count of most freq character <= k ?
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 +count.get(s[r],0)
            while (r - l + 1) - max(count.values()) > k:
                #decrement count of the left position by 1
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res