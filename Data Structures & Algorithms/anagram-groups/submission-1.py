class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #mappig character count to list of anagrams

        for word in strs:
            count = [0] * 26 # a-z

            for character in word:
                count[ord(character) - ord("a")] += 1
            
            res[tuple(count)].append(word)
        return list(res.values())