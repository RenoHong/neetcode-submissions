class Solution {
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        process(candidates, 0, target, new ArrayList<Integer>());
        return res ;
    }

    void process(int[] candidates, int index, int remain, List<Integer> path){
        if(remain == 0){ 
            res.add( new ArrayList<>(path)) ;
            return ;
        }

        for(int i = index ; i < candidates.length ; i++){
            if(candidates[i] > remain){
                break;
            }

            if(i > index && candidates[i] == candidates[i-1]){
                continue;
            } 
            path.add(candidates[i]) ;
            process(candidates, i + 1, remain - candidates[i], path);
            path.remove(path.size() -1 );
            
        }
    }
}
