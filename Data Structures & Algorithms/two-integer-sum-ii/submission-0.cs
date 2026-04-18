public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        Dictionary<int, int> dict = new Dictionary<int, int>() ;
        for(int i =0 ; i< numbers.Length ; i++){
            int remain = target - numbers[i];
            if(dict.ContainsKey(remain)){
                return new int[]{dict[remain]+1, i +1};
            }else{
                dict[numbers[i]] = i ;
            }
        }
        return new int[]{-1,-1} ;
    }
}
