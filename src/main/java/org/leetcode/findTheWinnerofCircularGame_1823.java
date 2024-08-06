package org.leetcode;

import java.util.ArrayList;

public class findTheWinnerofCircularGame_1823 {
    public int findTheWinner(int n, int k) {
        return recursion(n, k) + 1;
    }

    public int recursion(int n, int k){
        if(n == 1){
            return 0;
        }
        return (recursion(n - 1, k) + k) % n;
    }

    public int findTheWinner1(int n, int k) {
        ArrayList<Integer> circle = new ArrayList<>();
        for(int i = 0; i < n; i++){
            circle.add(i+1);
        }
        int idx = 0;
        while(circle.size() > 1){
            int next = (idx + k - 1) % circle.size();
            circle.remove(next);
            idx = next;
        }

        return circle.get(0);
    }
}
