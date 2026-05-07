class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            if (r not in range(ROWS) 
            or c not in range(COLS) 
            or grid[r][c]==0):
                return 0
            area = 1
            grid[r][c] = 0
        
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        best = 0

        for r in range (ROWS):
            for c in range (COLS):
                best = max(best, dfs(r,c))
        return best