class Solution {

    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        
        process(nums, 0, target, new ArrayList<Integer>());
        return res ;
    }

    void process(int[] nums, int index, int remain,  List<Integer> path){
        
         if(remain < 0 ) return ;
         if(remain == 0){
            res.add(new ArrayList<>(path)) ;
            return ;
         }

         for(int i = index ; i < nums.length ; i++){
            path.add(nums[i]);
            process(nums, i, remain - nums[i], path) ;
            path.remove(path.size() -1);
         }
    }
}

