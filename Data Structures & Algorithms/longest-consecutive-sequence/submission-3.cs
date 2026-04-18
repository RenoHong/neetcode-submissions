public class Solution {
    public int LongestConsecutive(int[] nums) {
        if(nums == null || nums.Length == 0)
            return 0;
        if(nums.Length == 1) return 1 ;
        var list = new HashSet<int>(nums).ToList<int>() ;
        list.Sort() ;
        int ans = 1 ;
        int max = 1 ;
        int? pre = null ;
        for(int i =0 ; i< list.Count; i++){
            if(pre == null){
                pre = list[i] ;
            }else{
                if(pre + 1 == list[i]){
                    ans ++ ;
                    max = Math.Max(max, ans) ;
                }else{
                    ans = 1 ;
                }
                pre = list[i] ;
            }
        }
        return max ;
    }
}
