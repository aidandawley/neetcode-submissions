class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        checker = {")" : "(", "]" : "[", "}" : '{'}

        for char in s:
            #we only insta kill program ever if we get a bad closing
            #lets check if we have a closing by using our dictionary
            if char in checker:
                #we have a closing!
                #lets check if the closing isnt in an empty stack
                #lets check that the closing matches 

                if stack and stack[-1] == checker[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        return True if not stack else False
                

