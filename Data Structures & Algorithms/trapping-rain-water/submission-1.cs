public class Solution {
    public int Trap(int[] height) {
        if(height == null || height.Length <2){
            return 0; 
        }

        int ans = 0 ; 
        int l =0 ;
        int r = height.Length -1 ;
        int leftMax = height[l] ;
        int rightMax = height[r] ;


        while(l<r){
            if(leftMax <= rightMax){
                l++ ;
                if(height[l] < leftMax){
                     ans += leftMax - height[l] ;
                }else{
                    leftMax = height[l];
                }
            }else{
                r--;
                if(height[r] < rightMax){
                    ans += rightMax - height[r];
                }else{
                    rightMax = height[r] ;
                }
            }
        }

        return ans ;
    }
}
