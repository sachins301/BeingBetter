package org.leetcode;

public class firstUniqueCharacterInAString_387 {
    public int firstUniqChar(String s) {
        int res = s.length()+1;
        for(char c = 'a'; c <= 'z'; c++){
            int index = s.indexOf(c);
            if (index != -1 && index == s.lastIndexOf(c))
                res = Math.min(res, index);
        }
        return res == s.length()+1 ? -1 : res;
    }
}
