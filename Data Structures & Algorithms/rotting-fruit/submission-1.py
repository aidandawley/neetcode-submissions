class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue= collections.deque()
        
        #need to be able to check if any fresh left
        freshCount = 0
        time = 0

        #we initialize our freshcount and our beggining rotten oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    freshCount += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    grid[r][c] = 0
        directions = [[0,1],[0, -1], [1,0], [-1,0]]
        #bfs
        while freshCount > 0 and queue:
            size = len(queue)

            #loop through our current queue
            for i in range(size):
                r, c = queue.popleft()

                #constant 4 iteration loop
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    #now lets check what its touching
                    #check 1.its in bounds 2.
                    if (row in range(len(grid))
                    and col in range(len(grid[0])) 
                    and grid[row][col] == 1):
                        #set it to rotten, append it to queue, remove fresh
                        grid[row][col] = 2
                        queue.append((row,col))
                        freshCount -= 1
            time += 1
            #need to be prepared for edge case
            #sometimes fresh fruit is unreachable
        return time if freshCount ==0 else -1


            

