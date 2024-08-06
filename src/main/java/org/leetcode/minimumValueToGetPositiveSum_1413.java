package org.leetcode;

public class minimumValueToGetPositiveSum_1413 {
    public int minStartValue(int[] nums) {
        int res = 1;
        int sum = 1;
        for(int i: nums){
            sum += i;
            if(sum < 1){
                res += 1 - sum;
                sum = 1;
            }
        }
        return res;
    }
}
