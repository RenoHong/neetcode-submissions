public class Solution {
    public int MaxArea(int[] heights) {
        int ans = 0 ; 
        int l = 0 , r = heights.Length -1 ;
        while(l < r){
            int lv = heights[l] ;
            int rv = heights[r] ;
            int min = Math.Min(lv, rv) ;

            ans = Math.Max(ans, min * (r-l));

            if(lv < rv) {
                l++;
            }else{
                r--;
            }

        }
        

        return ans ;

    }
}
