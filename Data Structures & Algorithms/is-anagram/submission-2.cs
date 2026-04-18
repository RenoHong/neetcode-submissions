public class Solution {
    public bool IsAnagram(string s, string t) {
        
        if(String.IsNullOrEmpty(s) && String.IsNullOrEmpty(s)) return true;
        if( (!String.IsNullOrEmpty(s) && String.IsNullOrEmpty(s)) ||
            (String.IsNullOrEmpty(s) && !String.IsNullOrEmpty(s)) 
        ) 
            return false;
       
        if(s.Length != t.Length) return false ;

        int[] table = new int[26];
        for(int i =0;i< s.Length;i++){
            table[s[i] - 'a'] ++ ;
            table[t[i] - 'a'] --;
        }
        foreach(int i in table){
            if(i != 0) return false;
        } 
        return true ;
    }
}
