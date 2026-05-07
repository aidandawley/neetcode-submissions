class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #run bfs if the start letters match
        # we want to see a return chain of all trues for something to be true
        #also keep track of the len of a word

        word = list(word)
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c,currentLength):
            if (r not in range(ROWS)
                or c not in range(COLS)
                or board[r][c] != word[currentLength]):
                return False
            if currentLength == len(word) - 1:
                return True
            
            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                if dfs(dr+r,dc+c,currentLength + 1):
                    return True
            
            board[r][c] = temp

            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        
        return False

            

