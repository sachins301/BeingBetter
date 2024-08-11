package org.leetcode;

import java.util.HashMap;
import java.util.Map;

public class fractionToRecurringDecimals_166 {
    public String fractionToDecimal(int numerator, int denominator) {
        if(numerator == 0 || denominator == 0)
            return "0";
        StringBuilder res = new StringBuilder();
        if((numerator < 0) != (denominator < 0))
            res.append("-");
        long num = Math.abs((long)numerator);
        long den = Math.abs((long)denominator);
        res.append(num/den);
        long rem = num % den;
        Map<Long, Integer> seen = new HashMap<>();
        if(rem == 0)
            return res.toString();
        res.append(".");
        while(rem != 0){
            if(seen.containsKey(rem)){
                res.insert(seen.get(rem), "(");
                res.append(")");
                break;
            }
            seen.put(rem, res.length());
            rem *= 10;
            res.append(Long.toString(rem / den));
            rem %= den;

        }
        return res.toString();
    }
}
