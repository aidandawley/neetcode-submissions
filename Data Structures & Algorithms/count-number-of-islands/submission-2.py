class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islandCount = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c):
            if (r not in range(ROWS)
            or c not in range(COLS)
            or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                row = dr + r
                column = dc + c

                dfs(row,column)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islandCount +=1
                    dfs(r,c)
        return islandCount
                    