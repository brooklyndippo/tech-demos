from multiprocessing.sharedctypes import Value


class Solution(object):
    def isValidSudoku(self, board):
        board = board
        self.checkBoard()

    def checkBoard(self):
        row_error = self.invalidRow()
        column_error = self.invalidColumn()
        grid_error = self.invalidGrid()
        if row_error or column_error or grid_error:
            print("This sodoku is not valid.")
            return False
        else:
            print("This sodoku board is valid!")
            return True


    def invalidRow(self):
        for row in board:
            dot = "."
            try:
                while True:
                    row.remove(dot)
            except ValueError:
                pass
            print (row)
            print (set(row))
            
            if len(row) != len(set(row)):
                print("Invalid Row.")
                return True
        else:
            return False

    def invalidColumn(self):
        index = 0
        while index < len(board):
            column = []
            for row in board:
                column.append(row[index])
                if len(column) == len(row):
                    dot = "."
                    try:
                        while True:
                            column.remove(dot)
                    except ValueError:
                        pass
                    print (column)
                    print (set(column))
                    if len(column) != len(set(column)):
                        print("Invalid Column.")
                        return True
                    else:
                        index += 1


    def invalidGrid(self):
        # use modulus to find the fence posts
        # group_num = len(board) % 3 ==> 3
        # index = 0
        # while index < group_num
        #   bottom = index*3
        #   top = (index+1)*3
        #   grid_row = board[bottom:top] 
            #count = 0
            #while total_grids < len(board)
            #for row in grid_row: 
                    #   grid = []
                    #   bottom = count*3
                    #   top = (count+1)*3
                    #   grid.append(row[bottom:top])
                # when grid length == 9:
                    #call the helper function to check for repeats
                    #if not repeating?:
                    #count += 1
                    #total_grids += 1
            #index += 1
                
        pass
    



#----------------------------
#-------PROBLEMS-------------
#----------------------------

problem = Solution()

# EXAMPLE 1 
# input

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


# output 
# --> true

problem.isValidSudoku(board)

#----------------------------

# EXAMPLE 2 
# input

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


# output 
# --> false

problem.isValidSudoku(board)