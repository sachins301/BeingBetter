package org.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class shortestSubarrayWithSumK_862 {
    public int shortestSubarray(int[] nums, int k) {
        int n = nums.length;
        int res = n + 1;
        long[] sum = new long[n + 1];
        for(int i = 0; i < n; i++)
            sum[i + 1] = sum[i] + nums[i];
        Deque<Integer> d = new ArrayDeque<>();
        for(int i = 0; i < n + 1; i++){
            while(d.size() > 0 && sum[i] - sum[d.getFirst()] >= k){
                res = Math.min(res, i - d.pollFirst());
            }
            while(d.size() > 0 && sum[d.getLast()] > sum[i])
                d.pollLast();
            d.addLast(i);
        }
        return res <= n ? res : -1;
    }
}
