public class Solution {
    public int MaxProfit(int[] prices) {
        int maxProfit = 0 ; 
        int minBuy = prices[0] ;
        foreach(int p in prices){
            maxProfit = Math.Max(maxProfit, p - minBuy) ;
            minBuy = Math.Min(p, minBuy);
        }
        return maxProfit; 
    }
}
