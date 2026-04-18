public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> dict = new Dictionary<string, List<string>>() ;
        foreach(var s in strs){
            int[] ints = new int[26];
            foreach(char c in s){
                ints[c - 'a']++;
            }
            string key = String.Join(",", ints) ;
            if(!dict.ContainsKey(key))
            {
                dict[key] = new List<string>();
            } 
            dict[key].Add(s); 
        } 
        return dict.Values.ToList() ; 
    }
    
  
}
