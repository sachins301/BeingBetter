package org.leetcode;

public class minimizeSizeSubarraySum_209 {
    public int minSubArrayLen(int target, int[] nums) {
        int res = nums.length+1;
        int i = 0, j = 0;
        int sum = nums[0];
        while(i <= j && i < nums.length){
            if(sum >= target || j == nums.length){
                if(sum >= target)
                    res = Math.min(res, j - i + 1);
                sum -= nums[i];
                i += 1;
            }
            else{
                j += 1;
                if( j == nums.length)
                    continue;
                sum += nums[j];
            }
        }
        if(res == nums.length+1)
            return 0;
        return res;
    }
}
