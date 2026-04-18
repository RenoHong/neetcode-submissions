public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        return strs.GroupBy(s=> {
            char[] chars = s.ToCharArray();
            System.Array.Sort(chars);
            return new String(chars) ;
        })
        .Select(g => g.ToList())
        .ToList();
    }
    
  
}
