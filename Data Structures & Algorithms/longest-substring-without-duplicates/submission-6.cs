public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int ans =0 ;
        int l = 0 ;
        HashSet<char> set = new HashSet<char>();
        for (int r = 0; r < s.Length ; r++){
            while(set.Contains(s[r])){
                set.Remove(s[l]);
                l++ ;
            }
            set.Add(s[r]);
            ans = Math.Max(ans, r - l + 1) ;
        }
        return ans;
        
    }
}
