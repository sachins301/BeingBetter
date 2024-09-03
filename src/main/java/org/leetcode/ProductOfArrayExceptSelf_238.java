package org.leetcode;

import java.util.Arrays;

public class ProductOfArrayExceptSelf_238 {
    public int[] productExceptSelf(int[] nums) {
        int pre = 1;
        int[] res = new int[nums.length];
        Arrays.fill(res, 1);
        for(int i = 0; i < nums.length; i++){
            res[i] *= pre;
            pre *= nums[i];
        }
        int post = 1;
        for(int i = nums.length - 1; i >= 0; i--){
            res[i] *= post;
            post *= nums[i];
        }

        return res;
    }
}
