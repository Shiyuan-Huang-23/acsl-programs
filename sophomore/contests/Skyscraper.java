import java.util.*;

public class Skyscraper {
	//Board that game will be based off of
	static int[][] board = new int[6][6];
	//Global variables for coordinates of blank tiles
	static int row = 0;
	static int col = 0;
	
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 6; i++) {
			System.out.print("Enter the input: ");
			input = new Scanner(System.in);
			String inputStr = input.nextLine();
			//The first line of input sets up the board
			if(i == 0) {
				String[] inputArr = inputStr.split(" ");
				setBoard(inputArr);
				solve();
			} else {
				printTile(inputStr);
			}
		}
		
	}
	
	//Sets up the board with the first line of input
	//Runs common strategies
	public static void setBoard(String[] inputArr) {
		//Set up top clues
		for(int i = 0; i < 4; i++) {
			board[0][i + 1] = Integer.parseInt(inputArr[0].substring(i, i + 1));
		}
		//Set up clues for rows
		for(int i = 1; i < 5; i++) {
			if(inputArr[i].length() == 2) {
				board[i][0] = Integer.parseInt(inputArr[i].substring(0, 1));
				board[i][5] = Integer.parseInt(inputArr[i].substring(1, 2));
			} else {
				for(int j = 0; j < 6; j++) {
					board[i][j] = Integer.parseInt(inputArr[i].substring(j, j + 1));
				}
			}
		}
		//Set up bottom clues
		for(int i = 0; i < 4; i++) {
			board[5][i + 1] = Integer.parseInt(inputArr[5].substring(i, i + 1));
		}
		//Run strategies
		strategies();
	}
	
	//Solves the board by recursion until the board matches clues
	public static boolean solve() {
		//If the clues don't match up, it's the wrong assignment
		if(!checkClue()) {
			return false;
		}
		
		//The board is solved if it's filled and the clues check out
		if(isFilled()) {
			return true;
		} 
		
		//Copy the coordinates of the unassigned tile for proper recursion
		int rowCopy = row;
		int colCopy = col;
		
		//The board isn't filled, and the current assignment matches clues
		for(int i = 1; i < 5; i++) {
			//Check to see if i is already in the same row or column
			if(isLegal(i, rowCopy, colCopy)) {
				//Assign the number to the blank tile
				board[rowCopy][colCopy] = i;
				//Recursive call
				if(solve()) {
					return true;
				}
				//Wipe tile if this assignment doesn't work
				board[rowCopy][colCopy] = 0;
			}
		}
		return false;
	}
	
	
	//A method that determines if the board currently matches the clues
	public static boolean checkClue() {
		boolean complete;
		//Checks to see if a row is filled
		for(int i = 1; i < 5; i++) {
			complete = true;
			for(int j = 1; j < 5; j++) {
				if(board[i][j] == 0) {
					complete = false;
				}
			}
			//If the row is filled, calculate the clues for that row
			if(complete) {
				int leftClue = 0;
				int rightClue = 0;
				int leftTemp = 0;
				int rightTemp = 0;
				for(int j = 1; j < 5; j++) {
					if(board[i][j] > leftTemp) {
						leftTemp = board[i][j];
						leftClue++;
					}
					if(board[i][5 - j] > rightTemp) {
						rightTemp = board[i][5 - j];
						rightClue++;
					}
				}
				//Check to see if calculated clues match board clues
				if(leftClue != board[i][0] || rightClue != board[i][5]) {
					return false;
				}
			}
		}
		
		//Checks to see if a column is filled
		for(int i = 1; i < 5; i++) {
			complete = true;
			for(int j = 1; j < 5; j++) {
				if(board[j][i] == 0) {
					complete = false;
				}
			}
			//If the column is filled, calculate the clues for that column
			if(complete) {
				int upClue = 0;
				int downClue = 0;
				int upTemp = 0;
				int downTemp = 0;
				for(int j = 1; j < 5; j++) {
					if(board[j][i] > upTemp) {
						upTemp = board[j][i];
						upClue++;
					}
					if(board[5 - j][i] > downTemp) {
						downTemp = board[5 - j][i];
						downClue++;
					}
				}
				//Check to see if calculated clues match board clues
				if(upClue != board[0][i] || downClue != board[5][i]) {
					return false;
				}
			}
		}
		return true;
	}
	
	//Checks whether the puzzle is completely filled in
	//Assigns coordinates of first blank tile it sees
	public static boolean isFilled() {
		for(int i = 1; i < 5; i++) {
			for(int j = 1; j < 5; j++) {
				if(board[i][j] == 0) {
					//Assign the coordinates of the first blank tile
					row = i;
					col = j;
					return false;
				}
			}
		}
		return true;
	}
	
	//Checks whether an assignment is legal
	public static boolean isLegal(int num, int rowCopy, int colCopy) {
		boolean legal = true;
		//Checks whether num already exists in that row
		for(int i = 1; i < 5; i++) {
			if(board[rowCopy][i] == num) {
				legal = false;
			}
		}
		//Checks whether num exists in that column
		for(int i = 1; i < 5; i++) {
			if(board[i][colCopy] == num) {
				legal = false;
			}
		}
		
		return legal;
	}
	
	public static void printTile(String inputStr) {
		String[] inputArr = inputStr.split("");
		int rowCoord = Integer.parseInt(inputArr[0]);
		int colCoord = Integer.parseInt(inputArr[1]);
		System.out.println(board[rowCoord][colCoord]);
	}
	
	public static void strategies() {
		//Iterate through top row
		for(int i = 1; i < 5; i++) {
			//If any clue is 4, fill that column with ascending order
			if(board[0][i] == 4) {
				for(int j = 1; j < 5; j++) {
					board[j][i] = j;
				}
			} 
			//If any clue is 1, fill the adjacent tile with 4
			if(board[0][i] == 1) {
				board[1][i] = 4;
			}
		}
		//Iterate through left 
		for(int i = 1; i < 5; i++) {
			//If any clue is 4, fill that row with ascending order
			if(board[i][0] == 4) {
				for(int j = 1; j < 5; j++) {
					board[i][j] = j;
				}
			} 		
			//If any clue is 1, fill the adjacent tile with 4
			if(board[i][0] == 1) {
				board[i][1] = 4;
			}
		}						
		//Iterate through right
		for(int i = 1; i < 5; i++) {
			//If any clue is 4, fill that row with ascending order
			if(board[i][5] == 4) {
				for(int j = 1; j < 5; j++) {
					board[i][5 - j] = j;
				}
			}
			//If any clue is 1, fill the adjacent tile with 4
			if(board[i][5] == 1) {
				board[i][4] = 4;
			}
		}
		//Iterate through bottom
		for(int i = 1; i < 5; i++) {
			//If any clue is 4, fill that column with ascending order
			if(board[5][i] == 4) {
				for(int j = 1; j < 5; j++) {
					board[5 - j][i] = j;
				}
			}
			//If any clue is 1, fill the adjacent tile with 4
			if(board[5][i] == 1) {
				board[4][i] = 4;
			}
		}
		
		for(int i = 1; i < 5; i++) {
			lookThree(i);
		}
		
		fillLast();
	}
	
	//Method that searches for a specific number (1-4) on the board and fills in the remaining number if three of the target already exists on the board
	public static boolean lookThree(int target) {
		int[] rows = new int[4];
		int[] cols = new int[4];
		int filled = 0;
		//Count the number of targets on the board
		for(int i = 1; i < 5; i++) {
			for(int j = 1; j < 5; j++) {
				if(board[i][j] == target) {
					rows[i - 1] = 1;
					cols[j - 1] = 1;
					filled++;
				}  
			}
		}
		//If there are three of the target on the board, fill in the last one
		if(filled == 3) {
			int rowCoord = 0;
			int colCoord = 0;
			for(int i = 0; i < 4; i++) {
				if(rows[i] == 0) {
					rowCoord = i + 1;
				}
				if(cols[i] == 0) {
					colCoord = i + 1;
				}  
			}
			board[rowCoord][colCoord] = target;
			return true;
		}
			//Return false if no changes have been made to the board
			return false;
	}  

	//Method that fills in the last remaining number if a row or column already has 3 numbers filled
	public static boolean fillLast() {
		int[] filled;
		int zeros;
		int colCoord = 0;
		int rowCoord = 0;
		int target;
		boolean changed = false;
		//Count the number of 0s in a row
		for(int i = 1; i < 5; i++) {
			filled = new int[4];
			zeros = 0;
			target = 0;
			for(int j = 1; j < 5; j++) {
				if(board[i][j] == 0) {
					zeros++;
				}
			}
			//If there is only one blank in the row, fill in the last number
			if(zeros == 1) {
				//Find the coordinate of the blank space
				for(int h = 1; h < 5; h++) {
					if(board[i][h] == 0) {
						colCoord = h;
					} else {
						filled[board[i][h] - 1] = 1;
					}
				}
				//Find the number that should be filled in
				for(int h = 0; h < 4; h++) {
					if(filled[h] == 0) {
						target = h + 1;
					}
				}
				//Fill in the last number
				board[i][colCoord] = target;
				changed = true;
			}
		}
			
		for(int i = 1; i < 5; i++) {
			filled = new int[4];
			zeros = 0;
			target = 0;
			for(int j = 1; j < 5; j++) {
				if(board[j][i] == 0) {
					zeros++;
				}
			}
			//If there is only one blank in the row, fill in the last number
			if(zeros == 1) {
				//Find the coordinate of the blank space
				for(int h = 1; h < 5; h++) {
					if(board[h][i] == 0) {
						rowCoord = h;
					} else {
						filled[board[h][i] - 1] = 1; 
					}
				}
				//Find the number that should be filled in
				for(int h = 0; h < 4; h++) {
					if(filled[h] == 0) {
						target = h + 1;
					}
				}
				//Fill in last number
				board[rowCoord][i] = target;
				changed = true;
			}
		}
		return changed;
	}
}

