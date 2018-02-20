import java.util.*;

/*
F4, 0, 2, 1
J1, 90, 2, 2
A4, 180, 1, 4
C2, 270, 2, 3

J1, 0, 1, 1
J1, 90, 2, 1
F9, 180, 2, 4
B3, 270, 1, 3
B9, 270, 2, 1
*/

public class Blokus {
    public static final int[][] PIECEA = {{1, 2}};
    public static final int[][] PIECEB = {{1, 2}, {0, 3}};
    public static final int[][] PIECEC = {{0, 1, 0}, {2, 3, 4}};
    public static final int[][] PIECED = {{0, 1}, {2, 3}, {4, 0}};
    public static int[][] board = new int[10][10];
    public static int numWays;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for(int i = 0; i < 5; i++) {
            for(int row = 0; row < board.length; row++) {
                for(int col = 0; col < board[row].length; col++) {
                    board[row][col] = 0;
                }
            }
            numWays = 0;
            System.out.print("Enter the input, separated by a comma and a space: ");
            String[] inputArr = in.nextLine().split(", ");
            draw(inputArr[0], PIECEA, Integer.parseInt(inputArr[1]), 1, false);
            String[] possCoords = locatePossibleCoords(Integer.parseInt(inputArr[2]));
            for(int row = 0; row < 10; row++) {
                for(int col = 0; col < 10; col++) {
                    if(isValid(row + 1)) {
                        if(board[row + 1][col] > 0) {
                            if(board[row][col] == 0) {
                                board[row][col] = -1;
                            }
                        }
                    }
                    if(isValid(row - 1)) {
                        if(board[row - 1][col] > 0) {
                            if(board[row][col] == 0) {
                                board[row][col] = -1;
                            }
                        }
                    }
                    if(isValid(col + 1)) {
                        if(board[row][col + 1] > 0) {
                            if(board[row][col] == 0) {
                                board[row][col] = -1;
                            }
                        }
                    }
                    if(isValid(col - 1)) {
                        if(board[row][col - 1] > 0) {
                            if(board[row][col] == 0) {
                                board[row][col] = -1;
                            }
                        }
                    }
                }
            }
            for(int j = 0; j < possCoords.length; j++) {
                for(int k = 0; k < 4; k++) {
                    draw(possCoords[j], PIECEA, k * 90, Integer.parseInt(inputArr[3]), true);
                    draw(possCoords[j], PIECEB, k * 90, Integer.parseInt(inputArr[3]), true);
                    draw(possCoords[j], PIECEC, k * 90, Integer.parseInt(inputArr[3]), true);
                    draw(possCoords[j], PIECED, k * 90, Integer.parseInt(inputArr[3]), true);
                }

            }
            if(numWays != 0) {
                System.out.println(numWays);
            } else {
                System.out.println("NONE");
            }
        }
    }

    public static void draw(String location, int[][] piece, int rotation, int tileNum, boolean temporary) {
        char[] locationArr = location.toCharArray();
        int locRow = 9 - (location.charAt(0) - 65);
        int locCol = Integer.parseInt(location.substring(1)) - 1;
        piece = rotate(piece, rotation);

        int tileNumRow = -1;
        int tileNumCol = -1;
        for(int row = 0; row < piece.length; row++) {
            for(int col = 0; col < piece[0].length; col++) {
                if(piece[row][col] == tileNum) {
                    tileNumRow = row;
                    tileNumCol = col;
                }
            }
        }
        boolean isValid = true;
        if(tileNumRow == -1 && tileNumCol == -1) {
            isValid = false;
        }
        int[][] boardCopy = new int[10][10];
        for(int row = 0; row < 10; row++) {
            boardCopy[row] = Arrays.copyOf(board[row], board[row].length);
        }
        for(int row = 0; row < piece.length; row++) {
            for(int col = 0; col < piece[0].length; col++) {
                int rowCoord = locRow + (row - tileNumRow);
                int colCoord = locCol + (col - tileNumCol);
                if(piece[row][col] != 0) {
                    if(rowCoord > - 1 && rowCoord < 10 && colCoord > -1 && colCoord < 10 && boardCopy[rowCoord][colCoord] == 0) {
                        boardCopy[rowCoord][colCoord] = piece[row][col];
                    } else {
                        isValid = false;
                        break;
                    }
                }
            }
        }
        if(temporary) {
            if(isValid) {
                numWays++;
            }
        } else {
            board = (int[][]) boardCopy.clone();
        }
    }

    // returns the rotated piece
    public static int[][] rotate(int[][] piece, int rotation) {
        int[][] newPiece;
        if(rotation == 90) {
            newPiece = new int[piece[0].length][piece.length];
            for(int row = 0; row < piece.length; row++) {
                for(int col = 0; col < piece[0].length; col++) {
                    newPiece[col][piece.length - row - 1] = piece[row][col];
                }
            }
        } else {
            newPiece = piece;
            for(int times = 0; times < rotation / 90; times++) {
                newPiece = rotate(newPiece, 90);
            }
        }
        return newPiece;
    }

    public static String[] locatePossibleCoords(int tileNum) {
        ArrayList<String> possCoords = new ArrayList<String>();
        int tileNumRow = -1;
        int tileNumCol = -1;
        for(int row = 0; row < board.length; row++) {
            for(int col = 0; col < board.length; col++) {
                if(board[row][col] == tileNum) {
                    tileNumRow = row;
                    tileNumCol = col;
                    break;
                }
            }
        }
        int[] arr = {-1, 1};
        for(int i = 0; i < arr.length; i++) {
            for(int j = 0; j < arr.length; j++) {
                boolean isValid = true;
                int possXCoord = tileNumRow + arr[i];
                int possYCoord = tileNumCol + arr[j];
                if(isValid(possXCoord) && isValid(possYCoord)) {
                    if(isValid(possXCoord + 1)) {
                        if(board[possXCoord + 1][possYCoord] != 0) {
                            isValid = false;
                        }
                    }
                    if(isValid(possXCoord - 1)) {
                        if(board[possXCoord - 1][possYCoord] != 0) {
                            isValid = false;
                        }
                    }
                    if(isValid(possYCoord + 1)) {
                        if(board[possXCoord][possYCoord + 1] != 0) {
                            isValid = false;
                        }
                    }
                    if(isValid(possYCoord - 1)) {
                        if(board[possXCoord][possYCoord - 1] != 0) {
                            isValid = false;
                        }
                    }
                    if(isValid) {
                        String coordString = Character.toString((char) (9 + 65 - possXCoord)) + Integer.toString(possYCoord + 1);
                        possCoords.add(coordString);
                    }
                }
            }
        }
        String[] coords = new String[possCoords.size()];
        coords = possCoords.toArray(coords);
        return coords;
    }

    public static boolean isValid(int coord) {
        return coord > -1 && coord < 10;
    }
}
