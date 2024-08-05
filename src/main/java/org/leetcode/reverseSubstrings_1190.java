package org.leetcode;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.stream.Collectors;

public class reverseSubstrings_1190 {
    public String reverseParentheses(String s) {
        Stack<Character> res = new Stack<>();
        for(char c: s.toCharArray()){
            if (c != ')')
                res.push(c);
            else{
                Queue<Character> subStack = new LinkedList<>();
                while(!res.isEmpty()){
                    char pop = res.pop();
                    if(pop == '(') break;
                    else subStack.add(pop);
                }
                while(!subStack.isEmpty()){
                    res.push(subStack.poll());
                }
            }
        }
        return res.stream().map(x -> x.toString()).collect(Collectors.joining(""));
    }
}
