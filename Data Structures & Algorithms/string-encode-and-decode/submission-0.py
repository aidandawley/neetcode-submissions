class Solution:

    def encode(self, strs: List[str]) -> str:
        #want to encode until single string
        res = ""

        for s in strs:
            #we need to only make one string
            #so we encode with the strings character len
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            #length from i-j not including j
            length = int(s[i:j])
            #skip the # and give us the entire string
            res.append(s[j+1 : j+1 + length])
            i = j+1+length
        return res