class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> row = new HashSet<>();
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[i][j] != '.'){
                    if(row.contains(board[i][j])){
                        return false;
                    }
                    else{
                        row.add(board[i][j]);
                    }
                }
            }
            row.clear();
        }
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[j][i] != '.'){
                    if(row.contains(board[j][i])){
                        return false;                
                     }
                    else{
                        row.add(board[j][i]);
                   }
                }
            }
            row.clear();
        }
      for (int nrow = 0; nrow < 9; nrow += 3) {
        for (int col = 0; col < 9; col += 3) {

            Set<Character> box = new HashSet<>();

            for (int i = nrow; i < nrow + 3; i++) {
                for (int j = col; j < col + 3; j++) {

                if (board[i][j] != '.') {
                    if (box.contains(board[i][j])) {
                        return false;
                    }
                    box.add(board[i][j]);
                }

            }
        }}}
        return true;      }

}
