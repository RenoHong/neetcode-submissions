public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        Array.Sort(nums) ;
        var res = new List<List<int>>();
        for(int i =0 ; i< nums.Length ; i++){
            if(nums[i] > 0 ) break;
            if(i > 0 && nums[i] == nums[i-1]) continue ;
            int l = i + 1 ;
            int r = nums.Length -1 ;
            while(l < r){
                int ret = nums[i] + nums[l] + nums[r];
                if(ret == 0){
                    res.Add(new List<int>(){nums[i], nums[l], nums[r]});
                    r -- ;
                    l ++;
                    while(l < r && nums[l] == nums[l -1]) l++;
                }
                else if(ret > 0){
                    r-- ;
                }
                else{
                    l++;
                }
            }
        }
        return res ;
    }
}
