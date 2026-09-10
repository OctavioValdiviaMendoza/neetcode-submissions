class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Square1 = self.isValidSquare(board,0,0)
        Square2 = self.isValidSquare(board,0,3)
        Square3 = self.isValidSquare(board,0,6)
        Square4 = self.isValidSquare(board,3,0)
        Square5 = self.isValidSquare(board,3,3)
        Square6 = self.isValidSquare(board,3,6)
        Square7 = self.isValidSquare(board,6,0)
        Square8 = self.isValidSquare(board,6,3)
        Square9 = self.isValidSquare(board,6,6)
        validRows = self.isValidRow(board)
        validColumns = self.isValidColumn(board)

        validSquares = Square1 and Square2 and Square3 and Square4 and Square5 and Square6 and Square7 and Square8 and Square9
        answer = validSquares and validRows and validColumns 
        return answer

    def isValidRow(self, board: List[List[str]]) -> bool:
        check_duplicates = []
        for i in range (0,9):
            check_duplicates = []
            for j in range (0,9):
                if board[i][j] not in check_duplicates and board[i][j] != '.':
                    check_duplicates.append(board[i][j])
                elif board[i][j] != '.':
                    return False
        return True
    
    def isValidColumn(self, board: List[List[str]]) -> bool:
        check_duplicates = []
        for i in range(0,9):
            check_duplicates = []
            for j in range(0,9):
                if board[j][i] not in check_duplicates and board[j][i] != '.':
                    check_duplicates.append(board[j][i])
                elif board[j][i] != '.':
                    return False   
        return True
    
    def isValidSquare(self, board: List[List[str]], start_row, start_column):
        check_duplicates = {}
        for i in range (start_row, start_row+3):
            for j in range(start_column, start_column+ 3):
                check_duplicates[board[i][j]] = check_duplicates.get(board[i][j], 0) + 1

        for key, value in check_duplicates.items():
            if value > 1 and key != '.':
                return False     
        return True