class Solution {
    List<String> res = new ArrayList<>(); 
    public List<String> generateParenthesis(int n) {
        
        backtrack(n, n, "");
        return res ;
    }


    void backtrack(int left, int right, String s){
        if(s.isEmpty()){
            s ="(";
            left-- ;
        }
        if(left == 0 && right == 0){
            res.add(s);
            return;
        }
        if(left >0){
            backtrack(left-1, right, s + "(");
        }
        if(right > left){
            backtrack(left, right-1, s+ ")");
        }
    }

}
