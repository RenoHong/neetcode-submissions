public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        var pq = new PriorityQueue<int, int>(Comparer<int>.Create( (a,b) => b.CompareTo(a) ) ) ;
        foreach(var i in nums){
            pq.Enqueue(i, i) ;
        }
        while( k> 1) {
            pq.Dequeue();
            k-- ;
        }
        return pq.Peek();
    }
}
