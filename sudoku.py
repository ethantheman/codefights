def sudoku(grid):
	# this program checks whether the input 9x9 array represents a solved sudoku puzzle.

    ## this block checks validity of each 3x3 subgrid
    if(len(set(subgrid(0,0,grid))) != 9 or 
    	len(set(subgrid(0,3,grid))) != 9 or 
    	len(set(subgrid(0,6,grid))) != 9 or 
    	len(set(subgrid(3,0,grid))) != 9 or 
    	len(set(subgrid(3,3,grid))) != 9 or 
    	len(set(subgrid(3,6,grid))) != 9 or 
    	len(set(subgrid(6,0,grid))) != 9 or 
    	len(set(subgrid(6,3,grid))) != 9 or 
    	len(set(subgrid(6,6,grid))) != 9): return False
    
    ## this block checks validity of each 9x1 column/row.
    for i in range(len(grid)):
        temp1 = []
        temp2 = []
        for j in range(len(grid)):
            temp1.append(grid[i][j])
            temp2.append(grid[j][i])
        if(len(set(temp1)) != 9 or len(set(temp2)) != 9): return False
    return True


    
def subgrid(x, y, grid):
	## this method fills an array with the digits contained in a 3x3 subgrid.
    temp = []
    for i in range(x,x+3):
        for j in range(y,y+3):
            temp.append(grid[i][j])
    return temp


  ## test cases:
  #1: PRINTS TRUE
print(sudoku(
 [[1,3,2,5,4,6,9,8,7], 
  [4,6,5,8,7,9,3,2,1], 
  [7,9,8,2,1,3,6,5,4], 
  [9,2,1,4,3,5,8,7,6], 
  [3,5,4,7,6,8,2,1,9], 
  [6,8,7,1,9,2,5,4,3], 
  [5,7,6,9,8,1,4,3,2], 
  [2,4,3,6,5,7,1,9,8], 
  [8,1,9,3,2,4,7,6,5]]))

  #2: PRINTS FALSE
print(sudoku(
 [[1,3,2,5,4,6,9,2,7], 
  [4,6,5,8,7,9,3,8,1], 
  [7,9,8,2,1,3,6,5,4], 
  [9,2,1,4,3,5,8,7,6], 
  [3,5,4,7,6,8,2,1,9], 
  [6,8,7,1,9,2,5,4,3], 
  [5,7,6,9,8,1,4,3,2], 
  [2,4,3,6,5,7,1,9,8], 
  [8,1,9,3,2,4,7,6,5]]))

#3: PRINTS FALSE
print(sudoku(
[[1,3,4,2,5,6,9,8,7], 
[4,6,8,5,7,9,3,2,1], 
[7,9,2,8,1,3,6,5,4], 
[9,2,3,1,4,5,8,7,6], 
[3,5,7,4,6,8,2,1,9], 
[6,8,1,7,9,2,5,4,3], 
[5,7,6,9,8,1,4,3,2], 
[2,4,5,6,3,7,1,9,8], 
[8,1,9,3,2,4,7,6,5]]))

#4: PRINTS FALSE
print(sudoku(
[[1,3,2,5,4,6,9,8,7], 
[4,6,5,8,7,9,3,2,1], 
[7,9,8,2,1,3,6,5,4], 
[9,2,1,4,3,5,8,7,6], 
[3,5,4,7,6,8,2,1,9], 
[6,8,7,1,9,2,5,4,3], 
[5,4,6,9,8,1,4,3,2], 
[2,7,3,6,5,7,1,9,8], 
[8,1,9,3,2,4,7,6,5]]))

#5: PRINTS FALSE
print(sudoku(
[[1,2,3,4,5,6,7,8,9], 
[4,6,5,8,7,9,3,2,1], 
[7,9,8,2,1,3,6,5,4], 
[1,2,3,4,5,6,7,8,9], 
[4,6,5,8,7,9,3,2,1], 
[7,9,8,2,1,3,6,5,4], 
[1,2,3,4,5,6,7,8,9], 
[4,6,5,8,7,9,3,2,1], 
[7,9,8,2,1,3,6,5,4]]))