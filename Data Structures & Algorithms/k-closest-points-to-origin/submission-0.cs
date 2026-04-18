public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        Array.Sort(points, (a, b)=> {
           long la = (long)(a[0]*a[0] + a[1]*a[1]);
           long lb = (long)(b[0]*b[0] + b[1]*b[1]);
           return la.CompareTo(lb) ;
        }) ; 

        var res = new int[k][];
        Array.Copy(points, res, k) ;
        return res ;
    }
}
