class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        rottenQ = collections.deque()
        freshCount = 0
        time = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    rottenQ.append((i,j))
                    

        while rottenQ and freshCount > 0:
            size = len(rottenQ)
            for i in range(size):
                r,c = rottenQ.popleft()

                for dr,dc in directions:
                    newR = dr + r
                    newC = dc + c
                    if (newR in range(ROWS) and
                        newC in range(COLS) and
                        grid[newR][newC] == 1):

                        freshCount -= 1
                        grid[newR][newC] = 2
                        rottenQ.append((newR,newC))
            time +=1
        
        if freshCount ==0:
            return time
        else:
            return -1
            

            


        