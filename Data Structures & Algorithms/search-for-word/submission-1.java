class Solution {
    public boolean exist(char[][] board, String word) {

        for (int r =0 ; r < board.length ; r++){
            for(int c =0 ; c < board[r].length ; c++){
                if (process(board, r,c, 0, word) == true) return true ;
            }
        }
        return false ;
    }

    boolean process(char[][] board, int x, int y, int index, String w){
        if(x < 0 || y < 0 || x > board.length -1 || y > board[0].length-1 ){
            return false ;
        }


        if(board[x][y] == w.charAt(index)){

            if(index == w.length()-1) return true ;
        
            board[x][y] = '#' ;
            boolean found = process(board, x-1, y, index+1, w) ||
                            process(board, x+1, y, index+1, w) ||
                            process(board, x, y-1, index+1, w) ||
                            process(board, x, y+1, index+1, w) ;
            board[x][y] = w.charAt(index) ;
            return found ;
        }else{
            return false;
        }
    }
    
}
