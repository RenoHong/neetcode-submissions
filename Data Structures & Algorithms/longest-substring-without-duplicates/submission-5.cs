public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int ans =0 ;
        for(int i = 0; i< s.Length; i++){
            var seen = new HashSet<char>() ;
            for(int j = i ; j < s.Length; j++){
                if(!seen.Contains(s[j])) {
                    seen.Add(s[j]);
                }
                else{
                   break;
                }
            }
            ans = Math.Max(ans, seen.Count);
        }
        return ans;
        
    }
}
