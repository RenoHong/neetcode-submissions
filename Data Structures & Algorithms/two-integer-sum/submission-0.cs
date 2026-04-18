public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int,int>() ;
        for(int i =0 ; i< nums.Length ; i++){
            int required = target - nums[i] ;
            if(dict.ContainsKey(required)){
                return new int[] {dict[required], i} ;
            }
            dict[nums[i]] = i ;
        }
        return new int[]{-1,-1} ;
    }
}
