package org.leetcode;

public class robotReturnToOrigin_657 {
    public boolean judgeCircle(String moves) {
        Integer[] pos = new Integer[]{0, 0};
        for(char c: moves.toCharArray()){
            if(c == 'U') pos[1] += 1;
            if(c == 'D') pos[1] -= 1;
            if(c == 'R') pos[0] += 1;
            if(c == 'L') pos[0] -= 1;
        }
        // System.out.println(pos[0] + " " + pos[1]);
        return pos[0] == 0 && pos[1] == 0;
    }
}
