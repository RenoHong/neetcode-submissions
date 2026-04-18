public class Solution {
    public bool IsPalindrome(string s) {
        int l = 0 ; 
        int r = s.Length -1 ;
       s = s.ToLower();
        while(l<r){
            while(l<r && !Char.IsLetterOrDigit(s[l])) l++;
            while(l<r && !Char.IsLetterOrDigit(s[r])) r--; 
            if(s[l] != s[r])
                return false ;
            l++ ;
            r--;
        }
        return true ;
    }
}
