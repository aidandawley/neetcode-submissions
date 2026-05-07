class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                
                if (value,r) in seen or (value, c, "col") in seen or (value, r//3, c//3) in seen:
                    return False
                
                seen.add((value, r))
                seen.add((value, c, "col"))
                seen.add((value, r//3, c//3))
        return True