public class Solution {
    public int MaxArea(int[] heights) {
        int ans = 0 ; 

        for(int i =0; i<heights.Length; i++){
            for(int j = i +1 ; j < heights.Length; j++){
                ans = Math.Max(ans, (j-i) * Math.Min(heights[i], heights[j]) );
            }
        }

        return ans ;

    }
}
