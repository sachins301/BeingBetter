package org.leetcode;

import java.util.HashMap;

public class SubArraySumEqualsK_560 {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> prefix = new HashMap<>();
        int sum = 0;
        int res = 0;
        for(int n: nums){
            sum += n;
            if(sum == k)
                res += 1;
            if(prefix.containsKey(sum - k))
                res += prefix.get(sum - k);
            prefix.put(sum, prefix.getOrDefault(sum, 0) + 1);
        }
        return res;
    }
}
