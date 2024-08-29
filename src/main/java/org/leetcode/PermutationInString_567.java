package org.leetcode;

import java.util.Arrays;

public class PermutationInString_567 {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()) return false;
        int[] s1Code = new int[26];
        int[] s2Code = new int[26];

        for(int i = 0; i < s1.length(); i++){
            s1Code[s1.charAt(i) - 'a']++;
            s2Code[s2.charAt(i) - 'a']++;
        }

        if(Arrays.equals(s1Code, s2Code)) return true;
        int i = 0;
        int j = s1.length();
        while(j < s2.length()){
            s2Code[s2.charAt(i) - 'a']--;
            s2Code[s2.charAt(j) - 'a']++;
            if(Arrays.equals(s1Code, s2Code)) return true;
            i++;
            j++;
        }

        return false;
    }
}
