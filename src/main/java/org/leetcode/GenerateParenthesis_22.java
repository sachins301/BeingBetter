package org.leetcode;

import java.util.ArrayList;
import java.util.List;

public class GenerateParenthesis_22 {
    public void recursive(int openCnt, int closeCnt, int n, String str, List<String> res){
        if(openCnt == n && closeCnt == n){
            res.add(str);
            return;
        }
        if(openCnt < n){
            recursive(openCnt + 1, closeCnt, n, str+"(", res);
        }
        if(closeCnt < openCnt){
            recursive(openCnt, closeCnt + 1, n, str+")", res);
        }
    }
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        recursive(0, 0, n, "", res);
        return res;

    }
}
