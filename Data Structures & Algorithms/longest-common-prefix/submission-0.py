class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #return the empty
        if not strs:
            return ""
        
        res = strs[0]
        for element in strs[1:]:
            while not element.startswith(res):
                res = res[:-1]
                if res == "":
                    return res
        
        return res