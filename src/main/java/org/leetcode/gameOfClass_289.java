package org.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class gameOfClass_289 {
    public void gameOfLife(int[][] board) {
        int[][] res = new int[board.length][];
        for (int i = 0; i < board.length; i++) {
            res[i] = Arrays.copyOf(board[i], board[i].length);
        }
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                ArrayList<Integer> neighbours = new ArrayList<>();
                if(i-1 >= 0)
                    neighbours.add(res[i-1][j]);
                if(i-1 >= 0 && j+1 < board[i].length)
                    neighbours.add(res[i-1][j+1]);
                if(j+1 < board[i].length)
                    neighbours.add(res[i][j+1]);
                if(i+1 < board.length && j+1 < board[i].length)
                    neighbours.add(res[i+1][j+1]);
                if(i+1 < board.length)
                    neighbours.add(res[i+1][j]);
                if(i+1 < board.length && j-1 >= 0)
                    neighbours.add(res[i+1][j-1]);
                if(j-1 >= 0)
                    neighbours.add(res[i][j-1]);
                if(i-1 >= 0 && j-1 >= 0)
                    neighbours.add(res[i-1][j-1]);
                int count_1 = Collections.frequency(neighbours, 1);
                if(res[i][j] == 1){
                    if(count_1 < 2)
                        board[i][j] = 0;
                    else if(count_1 == 2 || count_1 == 3 ){
                        continue;
                    }
                    else{
                        board[i][j] = 0;
                    }
                }
                else{
                    if(count_1 == 3)
                        board[i][j] = 1;
                }
            }
        }

        return;
    }
}
