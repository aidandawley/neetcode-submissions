class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS= len(matrix)
        COLS =len(matrix[0])

        top = 0
        bottom = ROWS-1
        #check bounds of each array
        while top <= bottom:
            #choose a middle row
            middle_row = (top + bottom) //2
            #top bound moves down one
            #if the last element in array is larger than target
            if target > matrix[middle_row][-1]:
                top = middle_row+1
            #bottom row moves up one
            #if the last element in array is smaller than target
            elif target < matrix[middle_row][0]:
                bottom = middle_row-1
            #if we got the correct row we leave while loop
            else:
                break
        
        #none of the rows contained the target
        if not (top <= bottom):
            return False

        #lets run the binary search on the row we found
        row = (top + bottom) //2

        left = 0
        right = COLS - 1

        while left <= right:
            middle = (right + left) //2
        
            if target > matrix[row][middle]:
                left = middle +1
            elif target < matrix[row][middle]:
                right = middle -1
            else:
                return True
        
        return False
          
            
            

            



        