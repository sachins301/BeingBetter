package org.leetcode;

public class bestTimeToBuyAndSellStock_121 {
    public int maxProfit(int[] prices) {
        int low = prices[0];
        int res = 0;
        for(int curr: prices){
            if(curr < low){
                low = curr;
            }
            else{
                res = Math.max(res, curr - low);
            }
        }
        return res;
    }
}
