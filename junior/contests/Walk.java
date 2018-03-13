/*
Test Input
4F9D39, DEB456, 3DA8B9, A57CA7, 26A84A, 2FCFA3, 3AAB09, 89CBF5

1, 2, L, 2
5, 3, A, 4
3, 5, B, 2
6, 7, R, 5
4, 7, L, 6

(2, 4)
(6, 4)
(4, 6)
(8, 7)
(3, 7)

Test Cases
Walking over edge of board
8, 5, B, 1
(1, 6)
8, 5, B, 2
(2, 7)

Walking into corner
8, 8, B, 1
(1, 1)
8, 8, B, 2
(2, 8)
8, 8, B, 3
(3, 1)
8, 8, B, 4
(3, 8)
8, 8, B, 5
(2, 1)
8, 8, B, 6
(1, 8)
8, 8, B, 7
(1, 1)
8, 8, B, 8
(2, 1)
8, 8, B, 9
(2, 2)
8, 8, B, 10
(1, 1)
8, 8, B, 11
(8, 2)
8, 8, B, 12
(1, 3)
8, 8, B, 13
(8, 3)
8, 8, B, 14
(7, 4)
8, 8, B, 15
(8, 5)

*/

// given an array of 8 hexadecimal values, converts each value to octal and fills in the array with the values
// it is given that there will be no 0s in the converted octal values

import java.util.*;

public class Walk {
    public static int[][] board;
    public static int rowCoord;
    public static int colCoord;
    
    public static void print2D(int[][] a) {
        for(int[] row : a) {
            for(int cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }

    public static void print2D(String[][] a) {
        for(String[] row : a) {
            for(String cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }
}    
