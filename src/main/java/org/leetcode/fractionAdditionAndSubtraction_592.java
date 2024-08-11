package org.leetcode;

public class fractionAdditionAndSubtraction_592 {
    public String fractionAddition(String expression) {
        int num = 0;
        int den = 1;
        int i = 0;
        while(i < expression.length()){
            int num1 = 0, den1 = 0;
            char sign = '+';
            if (expression.charAt(i) == '-' || expression.charAt(i) == '+') {
                sign = expression.charAt(i);
                i += 1;
            }
            while (i < expression.length() && Character.isDigit(expression.charAt(i))) {
                num1 = num1 * 10 + (expression.charAt(i) - '0');
                i += 1;
            }
            i += 1;
            while (i < expression.length() && Character.isDigit(expression.charAt(i))) {
                den1 = den1 * 10 + (expression.charAt(i) - '0');
                i += 1;
            }
            if(sign == '-')
                num1 *= -1;
            num = num * den1 + num1 * den;
            den *= den1;
            int gcd = gcd(Math.abs(num), den);
            num /= gcd;
            den /= gcd;
            System.out.println(num1 + "/" + den1);
        }
        return num + "/" + den;
    }
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
