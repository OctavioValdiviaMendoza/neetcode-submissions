class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        squares = {}

        #Checking both rows and cols in one pass O(n^2)
        for row in range(rows):
            rowCheck = set()
            colCheck = set()
            for col in range(cols):
                if board[row][col] != ".":
                    if board[row][col] in rowCheck:
                        return False
                    else:
                        rowCheck.add(board[row][col])
                if board[col][row] != ".":
                    if board[col][row] in colCheck:
                        return False
                    else:
                        colCheck.add(board[col][row])
                
                val = board[row][col]
                if val == ".":
                    continue
                box = (row//3, col//3)

                if box not in squares:
                    squares[box] = set()
                if val in squares[box]:
                    return False
                squares[box].add(val)
        return True
        