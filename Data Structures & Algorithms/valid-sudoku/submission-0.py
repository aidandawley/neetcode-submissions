class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if (val, r) in seen or (val, c, "col") in seen or (val, r // 3, c // 3) in seen:
                    return False

                seen.add((val, r))
                seen.add((val, c, "col"))
                seen.add((val, r // 3, c // 3))

        return True

