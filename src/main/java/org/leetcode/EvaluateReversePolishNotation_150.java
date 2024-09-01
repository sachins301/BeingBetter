package org.leetcode;

import java.util.Stack;

public class EvaluateReversePolishNotation_150 {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String s: tokens){

            if(s.equals("+")){
                stack.push(stack.pop() + stack.pop());
            } else if(s.equals("-")){
                Integer n = stack.pop();
                stack.push(stack.pop() - n);
            } else if(s.equals("*")){
                stack.push(stack.pop() * stack.pop());
            } else if(s.equals("/")){
                Integer n = stack.pop();
                stack.push(stack.pop() / n);
            } else{
                stack.push(Integer.valueOf(s));
            }
        }
        return stack.pop();
    }
}
