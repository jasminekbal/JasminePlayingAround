from random import randint, choice, shuffle


empty = [
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]]

posns = [(i, j) for j in range(9) for i in range(9)]
numberList=[1,2,3,4,5,6,7,8,9]


def print_board(board):
		for i in range (len(board)):
			if i%3 ==0 and i!= 0:
				print("-------------------------")
			for j in range(len(board[0])):
				if j%3 == 0 and j!= 0:
					print(" | ", end ="")
				if j == 8:
					print (board[i][j])
				else:
					print(str(board[i][j]) + " ", end = "")

def find_empty(board):
	for i in range (len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i, j) #row, col
	return None

def valid (board, num, posn):
	#check row
	for i in range(len(board[0])):
		if board[posn[0]][i] == num and posn[1] != i:
			return False
	# check column
	for i in range(len(board)):
		if board[i][posn[1]] == num and posn[0] != i:
			return False

	#check box
	box_x = posn[1] // 3
	box_y = posn[0] // 3

	#looping through the box
	for i in range (box_y *3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 +3):
			if board[i][j] == num and (i, j) != posn:
				return False

	return True

def solve (board):
	find = find_empty(board)

	if not find:
		return True
	else:
		row, col = find

	for i in range(1,10):
		if valid(board, i, (row, col)):
			board[row][col] = i

			if solve (board):
				return True

			board[row][col] = 0

	return False


#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def solveGrid(grid):
  global counter
  #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        #Check that this value has not already be used 
        if valid(grid, value,(row, col)):
              grid[row][col]=value
              if find_empty(grid) == None:
                counter +=1
                break
              else:
                if solveGrid(grid):
                  return True
      break
  grid[row][col]=0  


#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def fillGrid(grid):
  global counter
  #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      shuffle(numberList)      
      for value in numberList:
        if valid(grid, value,(row, col)):
              grid[row][col]=value
              if find_empty(grid) == None:
                return True
              else:
                if fillGrid(grid):
                  return True
      break
  grid[row][col]=0        




def make_board ():
	fillGrid(empty)
	board = empty
	global counter 

	while len(posns) != 0:
 		posn = posns.pop()
 		val = board[posn[0]][posn[1]]
 		board[posn[0]][posn[1]] = 0

 		copybo = list.copy(board)
 		
 		counter = 0
 		solveGrid(copybo)
 		if counter >1:
 			board[posn[0]][posn[1]] = val

	return board


new_board = make_board()

print_board(new_board)



 