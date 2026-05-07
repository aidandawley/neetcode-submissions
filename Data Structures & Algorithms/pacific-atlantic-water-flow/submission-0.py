class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS= len(heights)
        COLS= len(heights[0])

        pac = set()
        atl = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c,visitSet,prevHeight):
            if ((r,c) in visitSet 
            or r not in range(ROWS)
            or c not in range(COLS) 
            or heights[r][c] < prevHeight):
                return
            visitSet.add((r,c))
            for dr,dc in directions:
                dfs(r + dr, c+ dc, visitSet, heights[r][c])
            
        for c in range (COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range (ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        res = []    
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res