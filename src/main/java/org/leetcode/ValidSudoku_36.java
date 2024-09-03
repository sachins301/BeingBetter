package org.leetcode;

import java.util.HashSet;
import java.util.Set;

public class ValidSudoku_36 {
    public boolean isValidSudoku(char[][] board) {
        Set<String> row  = new HashSet<>();
        Set<String> col = new HashSet<>();
        Set<String> grid = new HashSet<>();
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[i][j] == '.')
                    continue;
                if(!row.add(i+ "" +board[i][j]) || !col.add(j + "" + board[i][j]) || !grid.add(i/3+""+j/3+""+board[i][j]))
                    return false;
            }
        }
        return true;
    }
}
