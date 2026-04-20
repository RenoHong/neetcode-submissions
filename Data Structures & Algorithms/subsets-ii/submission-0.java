class Solution {

    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> subsetsWithDup(int[] nums) {

        Arrays.sort(nums);
        process(nums,0, new ArrayList<Integer>());
        return res ;
    }

    void process(int[] nums, int index, List<Integer> path){
  
        res.add(new ArrayList<>(path));
         

        for(int i = index ; i< nums.length ; i++){

            if(i > index && nums[i] == nums[i-1]) continue; 
            path.add(nums[i]);
            process(nums, i + 1, path);
            path.remove(path.size() -1);
        }
    }
}
