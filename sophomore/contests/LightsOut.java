/*
* Shiyuan Huang
* Intermediate Division 3
* Grade 10
* Barrington High School
* Barrington RI
*/

import java.util.*;

public class LightsOut {
	//The default board that all game play will be based off of
	static int[][] board = new int[8][8];
	
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			//Accept the input
			System.out.print("Enter the input: ");
			input = new Scanner(System.in);
			String inputStr = input.nextLine();
			String[] inputArr = inputStr.split(" ");
			//Call the runRules function with the inputArr as an argument
			runRules(inputArr);
			//Reset the board to its original state
			board = new int[8][8];
		}
	}
	
	public static void runRules(String[] inputArr) {
		//Designate a variable for the number of rows
		int rows = Integer.parseInt(inputArr[0]);
		//Turn on the tiles that are supposed to be turned on
		for(int i = 0; i < rows; i++) {
			setBoard(inputArr[i + 1]);
		}
		//Designate a variable for the number of tile presses
		int presses = Integer.parseInt(inputArr[rows + 1]);
		//Press the tiles
		for(int i = 0; i < presses; i++) {
			press(inputArr[rows + i + 2]);
		}
		//Count the number of tiles on2 4
		countBoard();
	}
	
	public static void press(String pressCoords) {
		//Designate a variable for the row coordinate
		int rowCoord = Integer.parseInt(pressCoords.substring(0, 1));
		//Designate a variable for the column coordinate
		int columCoord = Integer.parseInt(pressCoords.substring(1, 2));
		//Invert the pressed button
		invert(rowCoord, columCoord);
		//Invert the top adjacent tile
		invert(rowCoord + 1, columCoord);
		//Invert the right tile
		invert(rowCoord, columCoord + 1);
		//Invert the bottom tile
		invert(rowCoord - 1, columCoord);
		//Invert the left tile
		invert(rowCoord, columCoord - 1);
		//Invert the four corners clockwise, starting from the top right
		invert(rowCoord + 1, columCoord + 1);
		invert(rowCoord - 1, columCoord + 1);
		invert(rowCoord - 1, columCoord - 1);
		invert(rowCoord + 1, columCoord - 1);
		//Invert the farthest tiles clockwise, starting from the top 
		invert(rowCoord + 2, columCoord);
		invert(rowCoord, columCoord + 2);
		invert(rowCoord - 2, columCoord);
		invert(rowCoord, columCoord - 2);
	}
	
	public static void setBoard(String coords) {
		//Designate a variable for the row coordinate
		int rowCoord = Integer.parseInt(coords.substring(0, 1));
		for(int i = 0; i < (coords.length() - 1); i ++) {
			//Designate a variable for the column coordinate
			int columCoord = Integer.parseInt(coords.substring(i + 1, i + 2));
			invert(rowCoord, columCoord);
		}
	}
	
	public static void invert(int rowCoord, int columCoord) {
		//Invert only if coordinates are valid
		if(rowCoord >= 1 && rowCoord <= 8) {
			if(columCoord >= 1 && columCoord <= 8) {
				//Convert the coordinates into actual position in the array
				rowCoord = 8 - rowCoord;
				columCoord = columCoord - 1;
				//Find the status of the position
				int status = board[rowCoord][columCoord];
				//Invert the status of the position
				if(status == 0) {
					board[rowCoord][columCoord] = 1;
				} else {
					board[rowCoord][columCoord] = 0;
				}
			}
		}
		
	}
	
	public static void countBoard() {
		//Iterate through the board and count the number of tiles on
		int numOn = 0;
		for(int i = 0; i < 8; i++) {
			for(int j = 0; j < 8; j++) {
				if(board[i][j] == 1) {
					numOn++;
				}
			}
		}
		System.out.println(numOn);
	}
}

