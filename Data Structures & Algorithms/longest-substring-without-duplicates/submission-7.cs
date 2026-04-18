public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int ans =0 ;
        int l = 0 ;
        Dictionary<char, int> dict = new Dictionary<char, int>(); 
        for(int r = 0 ; r < s.Length ; r++){
            if(dict.ContainsKey(s[r])){
                l = Math.Max(dict[s[r]] + 1, l);
            }
            dict[s[r]] = r ;
            ans = Math.Max(ans, r - l +1) ;
        }
        return ans;
        
    }
}
