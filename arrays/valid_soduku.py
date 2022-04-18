https://leetcode.com/problems/valid-sudoku

# sol1

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        digits = set()
        
        # check col values
        for i in range(len(board)):
            digits.clear()
            for j in  range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in digits:
                    digits.add(board[i][j])
                else:
                    print("col check failed")
                    return False
        
        # check row values
        for j in range(len(board[0])):
            digits.clear()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in digits:
                    digits.add(board[i][j])
                else:
                    return False
        
        # check grids
        r, c = len(board)-1, len(board[0])-1
        cr, cc = 0, 0
        k = 3
        while cr < r:
            while cc < c:
                digits.clear()
                for i in range(cr,cr+k):
                    for j in range(cc, cc+k):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] not in digits:
                            digits.add(board[i][j])
                        else:
                            return False
                cc += k
            cc = 0
            cr += k
        return True

#sol2

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            think of the grids as a matrix with 3X3 size
            we get which row or column of board is in the grid by dividing the row or col by 3
            
        """
        
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr != ".":
                    row_val = curr + " found in row " + str(i)
                    col_val = curr + " found in col " + str(j)
                    grid_val = curr + "found in grid " + str(i//3) + "," + str(j//3)
                    if row_val in visited or col_val in visited or grid_val in visited:
                        return False
                    visited.add(row_val)
                    visited.add(col_val)
                    visited.add(grid_val)
        return True