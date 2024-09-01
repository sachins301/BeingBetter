package org.leetcode;

import java.util.Map;
import java.util.Stack;

public class ValidParentheses_20 {

    public boolean isValid(String s) {
        if(s.length() % 2 == 1)
            return false;
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> closing = Map.of(
                '}', '{',
                ')', '(',
                ']', '['
        );
        for(Character c: s.toCharArray()){
            if(closing.containsKey(c)){
                if(stack.isEmpty() || stack.pop() != closing.get(c))
                    return false;
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();

    }

}
