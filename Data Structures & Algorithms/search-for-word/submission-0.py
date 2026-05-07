class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #we want to track the length of the word as we iterate
        #we need to return a sequence of trues when we find the correct
        #perform dfs on each and mark visited so we dont loop over the same ones
        ROWS = len(board)
        COLS = len(board[0])
        word = list(word)
        directions =[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c,charIndex):
            if (r not in range(ROWS)
                or c not in range(COLS)
                or board[r][c] != word[charIndex]):

                return False
            if charIndex == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                if dfs(dr+r,dc+c,charIndex+1):
                    return True
            
            board[r][c] = temp
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        
        return False




        