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

import java.util.*;

public class Walk {

    public static int[][] board;
    public static int rowCoord;
    public static int colCoord;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for(int i = 0; i < 6; i++) {
            if(i == 0) {
                System.out.print("Enter hexadecimal values, separated by a comma and a space: ");
                String[] hexValues = in.nextLine().split(", ");
                board = new int[8][8];
                makeBoard(hexValues);
            } else {
                System.out.print("Enter row, col, direction, and number of moves, separated by a comma and a space: ");
                String[] inputArr = in.nextLine().split(", ");
                rowCoord = 0;
                colCoord = 0;
                move(Integer.parseInt(inputArr[0]), Integer.parseInt(inputArr[1]), inputArr[2], Integer.parseInt(inputArr[3]));
                System.out.println(rowCoord + ", " + colCoord);
            }
        }
    }

    public static void move(int row, int col, String dirLetter, int movesLeft) {
        // ensures coordinates are valid
        if(row == 0) {
            row = 8;
        } else if(row == 9) {
            row = 1;
        }
        if(col == 0) {
            col = 8;
        } else if(col == 9) {
            col = 1;
        }
        // return the coordinates if there are no more moves left
        if(movesLeft == 0) {
            rowCoord = row;
            colCoord = col;
        } else {
            int[][] dirArray = letterToDirArray(dirLetter);
            String[][] coordArray = makeCoordArray(row, col);
            int angle = board[8 - row][col - 1] * 45;
            String destination = "";
            for(int i = 0; i < dirArray.length; i++) {
                for(int j = 0; j < dirArray[i].length; j++) {
                    if(dirArray[i][j] == angle) {
                        destination = coordArray[i][j];
                        break;
                    }
                }
            }
            movesLeft--;
            String[] destArr = destination.split(" ");
            String[] coords = destArr[0].split(",");
            move(Integer.parseInt(coords[0]), Integer.parseInt(coords[1]), destArr[1], movesLeft);
        }
    }

    public static String[][] makeCoordArray(int row, int col) {
        String[][] coordArray = new String[3][3];
        coordArray[0][0] = (row + 1) + "," + (col - 1) + " BR";
        coordArray[0][1] = (row + 1) + "," + col + " B";
        coordArray[0][2] = (row + 1) + "," + (col + 1) + " BL";
        coordArray[1][0] = row + "," + (col - 1) + " R";
        coordArray[1][1] = row + "," + col;
        coordArray[1][2] = row + "," + (col + 1) + " L";
        coordArray[2][0] = (row - 1) + "," + (col - 1) + " AR";
        coordArray[2][1] = (row - 1) + "," + col + " A";
        coordArray[2][2] = (row - 1) + "," + (col + 1) + " AL";
        return coordArray;
    }

    public static int[][] letterToDirArray(String d) {
        int[][] dirArray = null;
        if(d.equals("R")) {
            dirArray = rotate45(0);
        } else if(d.equals("AR")) {
            dirArray = rotate45(1);
        } else if(d.equals("A")) {
            dirArray = rotate45(2);
        } else if(d.equals("AL")) {
            dirArray = rotate45(3);
        } else if(d.equals("L")) {
            dirArray = rotate45(4);
        } else if(d.equals("BL")) {
            dirArray = rotate45(5);
        } else if(d.equals("B")) {
            dirArray = rotate45(6);
        } else if(d.equals("BR")) {
            dirArray = rotate45(7);
        }
        return dirArray;
    }

    public static int[][] rotate45(int times) {
        int[][] eightDir = new int[][] {{225, 270, 315}, {180, -1, 0}, {135, 90, 45}};
        for(int i = 0; i < times; i++) {
            int temp = eightDir[1][2];
            eightDir[1][2] = eightDir[2][2];
            eightDir[2][2] = eightDir[2][1];
            eightDir[2][1] = eightDir[2][0];
            eightDir[2][0] = eightDir[1][0];
            eightDir[1][0] = eightDir[0][0];
            eightDir[0][0] = eightDir[0][1];
            eightDir[0][1] = eightDir[0][2];
            eightDir[0][2] = temp;
        }
        return eightDir;
    }

    // given an array of 8 hexadecimal values, converts each value to octal and fills in the array with the values
    // it is given that there will be no 0s in the converted octal values
    public static void makeBoard(String[] hexValues) {
        for(int i = 0; i < hexValues.length; i++) {
            int decimalValue = Integer.parseInt(hexValues[i], 16);
            char[] octalValues = Integer.toOctalString(decimalValue).toCharArray();
            for(int j = 0; j < octalValues.length; j++) {
                board[7 - i][j] = octalValues[j] - 48;
            }
        }
    }

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
