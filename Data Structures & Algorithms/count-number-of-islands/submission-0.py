class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        q = collections.deque()

        def bfs(r,c):
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR = row + dr
                    newC = col + dc

                    if (newR in range(ROWS) 
                    and newC in range(COLS) 
                    and grid[newR][newC] == "1"):
                        q.append((newR,newC))
                        grid[newR][newC] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands