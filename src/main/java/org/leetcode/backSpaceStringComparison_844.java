package org.leetcode;

import org.jetbrains.annotations.NotNull;

import java.util.Stack;

class backSpaceStringComparison_844 {
    public boolean backspaceCompare(@NotNull String s, String t) {
        Stack<Character> s1 = new Stack<>();
        Stack<Character> t1 = new Stack<>();
        for(char c: s.toCharArray()){
            if(c == '#'){
                if(!s1.isEmpty())
                    s1.pop();
            } else {
                s1.push(c);
            }
        }

        for(char c: t.toCharArray()){
            if(c == '#'){
                if(!t1.isEmpty())
                    t1.pop();
            } else {
                t1.push(c);
            }
        }
        System.out.println(s1 + " " + t1);
        return s1.toString().equals(t1.toString());
    }
}