class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #need a hash tabel for our strings
        #lets use a count of all the letters in the array
        #we can use that count to access our string in the hash
        #the hash stores a tuple of all the strings with the key

        #default dict auto creates list for missing keys
        final_groups = defaultdict(list)

        #we will sort through the entire list of words
        for word in strs:
            count = [0] * 26
            #we will sort through all characters in the words
            for char in word:
                #this stors the count of the character on 
                #a 0-26 scale using asci values
                count[ord(char)- ord('a')] += 1
            #setting up the final hash with count as key
            final_groups[tuple(count)].append(word)
        return list(final_groups.values())