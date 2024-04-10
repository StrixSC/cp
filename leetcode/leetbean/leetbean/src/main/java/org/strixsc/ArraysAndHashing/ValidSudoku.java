package org.strixsc.ArraysAndHashing;

import java.util.HashSet;
import java.util.Set;

public class ValidSudoku {

    public static class Solution {
        public static boolean isValidSudoku(char[][] board) {
            // Traverse rows and check if duplicates are found;
            Set<Character> set = new HashSet<>();
            for (int row = 0; row < board.length; row++) {
                Set<Character> s = new HashSet<>();
                for (int col = 0; col < board[row].length; col++) {
                    char lookupValue = board[row][col];
                    if (lookupValue == '.') {
                        continue;
                    }

                    if (s.contains(lookupValue)) {
                        return false;
                    }

                    s.add(lookupValue);
                }
            }

            // Traverse columns and check if duplicates are found;
            for (int col = 0; col < board[0].length; col++) {
                Set<Character> s = new HashSet<>();
                for (int row = 0; row < board.length; row++) {
                    char lookupValue = board[row][col];
                    if (lookupValue == '.') {
                        continue;
                    }

                    if (s.contains(lookupValue)) {
                        return false;
                    }

                    s.add(lookupValue);
                }
            }

            // Traverse each 3x3 block and check if dupes are found
            for (int row = 0; row < board.length; row += 3) {
                for (int col = 0; col < board.length; col += 3)
                {
                    Set s = new HashSet();
                    for (int i = 0 ; i < 3; i++)
                    {
                        for (int j = 0; j < 3; j++)
                        {
                            char lookupValue = board[row + i][col + j];
                            if (lookupValue == '.')
                            {
                                continue;
                            }

                            if (s.contains(lookupValue))
                            {
                                return false;
                            }

                            s.add(lookupValue);
                        }
                    }
                }
            }

            return true;
        }

    }

    public static void main(String[] args) {
        System.out.println(
                Solution.isValidSudoku(
                        new char[][]{
                                {'.','.','4','.','.','.','6','3','.'},
                                {'.','.','.','.','.','.','.','.','.'},
                                {'5','.','.','.','.','.','.','9','.'},
                                {'.','.','.','5','6','.','.','.','.'},
                                {'4','.','3','.','.','.','.','.','1'},
                                {'.','.','.','7','.','.','.','.','.'},
                                {'.','.','.','5','.','.','.','.','.'},
                                {'.','.','.','.','.','.','.','.','.'},
                                {'.','.','.','.','.','.','.','.','.'}
                        }
                ));
    }
}
