public class Solution {
    public bool IsAnagram(string s, string t) {
        
        if(String.IsNullOrEmpty(s) && String.IsNullOrEmpty(s)) return true;
        if( (!String.IsNullOrEmpty(s) && String.IsNullOrEmpty(s)) ||
            (String.IsNullOrEmpty(s) && !String.IsNullOrEmpty(s)) 
        ) 
            return false;
       
        if(s.Length != t.Length) return false ;

        var sList = s.OrderBy(c=> c).ToList();
        var tList = t.OrderBy(c=> c).ToList();
        for(int i =0 ; i< sList.Count ; i++)
            if(sList[i]!= tList[i]) 
                return false ;
        
        return true ;
         
    }
}
