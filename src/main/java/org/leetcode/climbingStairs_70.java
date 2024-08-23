package org.leetcode;

import java.util.HashMap;

public class climbingStairs_70 {
    public static HashMap<Integer, Integer> map = new HashMap<>();
    public int climbStairs(int n) {
        if(n == 1)
            return 1;
        else if(n == 2)
            return 2;
        if(map.containsKey(n))
            return map.get(n);
        int result = climbStairs(n-1) + climbStairs(n-2);
        map.put(n, result);

        return result;
    }
}