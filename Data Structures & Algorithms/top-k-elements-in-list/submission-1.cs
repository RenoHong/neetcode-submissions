public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> dict = new Dictionary<int, int>() ;
        for(int i =0 ; i< nums.Length ; i++){
            if(!dict.ContainsKey(nums[i])){
                dict[nums[i]] = 1;
            }
            else{
                dict[nums[i]] ++ ;
            }
        }

        List<int>[] buckets = new List<int>[nums.Length +1];
        foreach(var kv in dict){
            var key = kv.Key ;
            var value = kv.Value ;
            if(buckets[value] == null){
                buckets[value] = new List<int>();
            }
           buckets[value].Add(key);
        }

        List<int> ret = new List<int>();
        for(int i = buckets.Length -1 ; i>0; i--){
            var list = buckets[i] ;
            if(list != null){
                for(int j = 0 ;j < list.Count ; j++){
                  if(ret.Count == k)
                    return ret.ToArray();
                  ret.Add(list[j]);
                }
            }
        } 
        return ret.ToArray() ;

    }
}
 