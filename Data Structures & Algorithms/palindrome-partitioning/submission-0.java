class Solution {
    List<List<String>> res = new ArrayList<>();
    public List<List<String>> partition(String s) {
        process(s, 0 , new ArrayList<String>());
        return res ;
    }

    void process(String s, int index, List<String> path){
        if(index >= s.length()){ 
            res.add(new ArrayList<>(path));
            return ;
        } 

        for(int i = index ; i < s.length() ; i++){ 
            String sub = s.substring(index, i +1); 
            if(isPalindrome(sub)){
                path.add(sub);
                process(s, i + 1, path) ;
                path.remove(path.size() -1);
            }
        }
    }

    boolean isPalindrome(String s){
        if(s.length()==1)
            return true;

        int left = 0 , right = s.length() -1 ;
        while(left < right){
            if( s.charAt(left) != s.charAt(right)){
                return false;
            }
            left ++ ;
            right -- ;
        }
        return true ;
    }
}
