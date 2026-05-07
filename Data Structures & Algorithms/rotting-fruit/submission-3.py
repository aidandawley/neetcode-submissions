class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        freshCount = 0
        time = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount +=1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    grid[r][c] = 0

        while freshCount > 0 and queue:
            size = len(queue)
            for i in range(size):
                row, col = queue.popleft()
                for dr, dc in directions:
                    newR = row + dr
                    newC = col + dc

                    if (newR in range(ROWS)
                        and newC in range(COLS)
                        and  grid[newR][newC] == 1):
                        
                        queue.append((newR,newC))
                        freshCount -= 1
                        grid[newR][newC] = 0
            time +=1
        
        if freshCount == 0:
            return time
        else:
            return -1 

