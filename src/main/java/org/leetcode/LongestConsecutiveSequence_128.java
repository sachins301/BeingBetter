package org.leetcode;

import java.util.HashSet;

public class LongestConsecutiveSequence_128 {
    public int longestConsecutive(int[] nums) {
        var set = new HashSet<>();
        for(int n: nums)
            set.add(n);
        var res = 0;
        for(int n: nums){
            int cnt = 1;
            if(!set.contains(n-1)){
                while(set.contains(n + cnt)){
                    cnt += 1;
                }
            }
            res = Math.max(res, cnt);
        }
        return res;
    }
}
