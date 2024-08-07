package org.leetcode;

import java.util.HashSet;
import java.util.Set;

public class jumpGameIII_1306 {
    public boolean canReach(int[] arr, int start){
        Set<Integer> seen = new HashSet<>();
        return canReachRec(arr, start, seen);
    }

    public boolean canReachRec(int[] arr, int start, Set<Integer> seen) {
        if(arr[start] == 0)
            return true;
        if(seen.contains(start))
            return false;
        seen.add(start);
        boolean res = false;
        if(start + arr[start] < arr.length)
            res = canReachRec(arr, start + arr[start], seen);
        if(res != true && start - arr[start] >= 0)
            res = canReachRec(arr, start - arr[start], seen);
        return res;
    }
}
