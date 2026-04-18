public class Solution {

    public string Encode(IList<string> strs) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i< strs.Count ; i++){
            
            sb.Append($"{strs[i].Length}#{strs[i]}");
             
        }
        return sb.ToString();
    }

    public List<string> Decode(string s) {
        int l = 0 ; 
        List<string> strs = new List<string>();
        while(l< s.Length){
            int r = l ;
            while(s[r]!='#'){
                r++ ;
            }
            int sz = Convert.ToInt32(s.Substring(l, r -l));
            string str = s.Substring(r+1, sz);
            l = r+sz +1 ;
            strs.Add(str);
        }
        return strs ;
   }
}
