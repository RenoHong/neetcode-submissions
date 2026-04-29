class Solution {

    List<List<String>> res = new ArrayList<>();
    public List<List<String>> solveNQueens(int n) {

        char[][] chess = new char[n][n] ;
        for(int r =0 ; r<chess.length; r++){
            Arrays.fill(chess[r], '.');
        }

        backtrack(chess, 0) ;
        return res ; 
    }

    void backtrack(char[][] chess, int row){
        if(row == chess.length){
            res.add(construct(chess));
        }
        for(int col = 0 ; col < chess.length ; col++){
            
            if(isValid(chess, row, col)){
                chess[row][col] ='Q' ;
                backtrack(chess, row +1); 
                chess[row][col] ='.';
            }
            
        } 
    }


    boolean isValid(char[][] chess, int row, int col){
        for(int i =0 ; i < row ; i++){
            for (int j=0; j < chess[i].length; j++){
                if(chess[i][j] == 'Q'){
                    if(j == col || Math.abs(col - j) == Math.abs(row-i)) 
                        return false ;
                }
            }
        }
        return true ;
    }

    List<String> construct(char[][]chess){
        List<String> list = new ArrayList<>();
        for (int i = 0; i< chess.length; i++)
            list.add(new String(chess[i]));
        return list;
    }
    

}
