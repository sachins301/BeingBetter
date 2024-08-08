package org.leetcode;

public class stringCompression {
    public int compress(char[] chars) {
        StringBuilder res = new StringBuilder();
        res.append(chars[0]);
        int count = 1;
        for(int i = 1; i < chars.length; i++){
            if(chars[i] == chars[i-1]){
                count += 1;
            }
            else{
                if(count != 1){
                    res.append(String.valueOf(count));
                }
                res.append(chars[i]);
                count = 1;
            }
        }
        if(count != 1)
            res.append(String.valueOf(count));
        for(int i = 0; i < res.length(); i++)
            chars[i] = res.charAt(i);
        return res.toString().length();
    }
}
