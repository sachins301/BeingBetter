package org.leetcode;

import java.util.ArrayList;
import java.util.List;

public class removeComments_722 {
    public List<String> removeComments(String[] source) {
        List<String> res = new ArrayList<>();
        Boolean blockComment = false;
        StringBuilder resLine = new StringBuilder();
        for(String line: source){
            if(blockComment == false){
                resLine = new StringBuilder();
            }
            for(int i = 0; i < line.length(); i++){
                if(blockComment == false && line.charAt(i) == '/' && i+1 < line.length() && line.charAt(i+1) == '/')
                    break;
                else if(blockComment == false && line.charAt(i) == '/' && i+1 < line.length() && line.charAt(i+1) == '*'){
                    blockComment = true;
                    i += 2;
                }
                else if(blockComment == false)
                    resLine.append(line.charAt(i));
                if(blockComment == true && line.charAt(i) == '*' && i+1 < line.length() && line.charAt(i+1) == '/'){
                    blockComment = false;
                    i++;
                }

            }
            if(blockComment == false && resLine.length() > 0){
                res.add(resLine.toString());
                System.out.println(resLine.toString());
            }

        }
        return res;
    }
}
