package org.leetcode;

public class palindromeSubstring_647 {
    public int countSubstrings(String s){
        int res = 0;
        for(int mid = 0; mid < s.length(); mid ++){
            // Check odd substrings
            int l = mid-1;
            int r = mid+1;
            res += 1;
            while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                res += 1;
                l -= 1;
                r += 1;
            }

            // Check even substrings
            l = mid;
            r = mid+1;
            while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
                res += 1;
                l -= 1;
                r += 1;
            }
        }
        return res;
    }

    //Brute Force Method
    public int countSubstrings1(String s) {
        int count = 0;
        for(int i= 0; i<s.length(); i++){
            for(int j = i+1; j <= s.length(); j++){
                if (checkPalindrome(s.substring(i, j)))
                    count += 1;
            }
        }
        return count;

    }
    public Boolean checkPalindrome(String s){
        int i = 0;
        int j = s.length()-1;
        while(i <= j){
            if(s.charAt(i) != s.charAt(j))
                return false;
            i += 1;
            j -= 1;
        }
        return true;
    }
}
