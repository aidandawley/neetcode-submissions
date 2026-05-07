class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        ROWS = len(grid)
        COLS = len(grid[0])
        freshCount = 0
        q = collections.deque()
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and freshCount > 0:
            size = len(q)

            for i in range(size):
                r,c = q.popleft()
                grid[r][c] = 2
                for dr, dc in directions:
                    row = r+ dr
                    col = c+ dc

                    if (row in range(ROWS)
                    and col in range(COLS)
                    and grid[row][col] == 1):
                        q.append((row,col))
                        freshCount -= 1
                        grid[row][col] = 2
            time +=1
        if freshCount == 0:
            return time
        else:
            return -1
                
