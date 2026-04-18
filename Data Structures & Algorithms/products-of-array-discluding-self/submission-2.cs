public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int product = 1 ; 
        int zeros = 0 ; 
        int[] ans = new int[nums.Length];
        foreach(int n in nums){
            if(n != 0){
                product *= n ;
            }else{
                zeros++ ;
            }

        }

        if(zeros >1){
            return ans ;
        }
        if(zeros ==1){
            for(int i =0 ; i< ans.Length ; i++)
            {
                if(nums[i] == 0) {
                    ans[i] = product;
                }
                else
                    ans[i] = 0 ;
            }          
        }
        else{
            for(int i =0 ; i< ans.Length ; i++)
            {
                 ans[i] = product / nums[i] ;
            }
        }


        return ans ;

    }
}
