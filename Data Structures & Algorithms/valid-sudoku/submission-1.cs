public class Solution {
    public bool IsValidSudoku(char[][] board) {
    
        for(int row = 0; row< board.Length; row++){
            var set = new int[10];
            for(int col=0 ; col < board[row].Length; col++ ){
                char c = board[row][col] ;
                if(c != '.'){ 
                    if(set[c - '0'] > 0){
                        return false;
                    }
                    set[c - '0']++ ;
                }
            }
 
        }

        for(int col = 0 ;col < 9;col++){
            var set = new int[10];
            for(int row =0 ; row <9 ; row++){
                char c = board[row][col] ;
                if(c != '.'){ 
                    if(set[c - '0'] > 0){
                        return false;
                    }
                    set[c - '0']++ ;
                }
            }
           
        }

        for(int boxRow = 0 ; boxRow < 3 ; boxRow++){
            for(int boxCol = 0 ; boxCol < 3 ; boxCol++){
                var set = new int[10];
                for(int row =0 ; row < 3 ; row++){
                    for(int col =0 ; col < 3; col++){ 
                        int thisRow = boxRow *3 + row ;
                        int thisCol = boxCol *3 + col ;
                        char c = board[thisRow][thisCol] ;
                        if(c != '.'){ 
                            if(set[c - '0'] > 0){
                                return false;
                            }
                            set[c - '0']++ ;
                        }
                    }
                }
            }
        }
        
        return true ;
        
    }
} 
