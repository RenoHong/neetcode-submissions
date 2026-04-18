public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        
        int[] taskCount = new int[26];
        foreach(char c in tasks){
            taskCount[c - 'A']++;
        }

        int maxFreq = taskCount.Max();

        int ans =  (maxFreq -1) * (n+1)  + taskCount.Count(t=> t == maxFreq) ;
        return Math.Max(ans, tasks.Length) ;
    }
}
