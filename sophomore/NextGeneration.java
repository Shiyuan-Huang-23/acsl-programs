import java.util.*;

public class NextGeneration {
	
	static String[][] original = {
		{"A", "D", "D", "D", "D", "D", "D", "D", "D", "D"},
		{"A", "D", "D", "D", "D", "D", "D", "D", "D", "D"},
		{"D", "D", "D", "A", "D", "D", "D", "D", "D", "D"},
		{"D", "D", "D", "D", "A", "D", "D", "D", "D", "D"},
		{"D", "D", "A", "D", "D", "A", "D", "D", "D", "A"},
		{"D", "A", "D", "A", "A", "D", "D", "A", "D", "D"},
		{"D", "D", "A", "D", "D", "D", "D", "D", "A", "A"},
		{"D", "A", "D", "D", "D", "D", "D", "D", "D", "A"},
		{"A", "D", "D", "D", "D", "D", "D", "D", "D", "A"},
		{"D", "D", "D", "D", "D", "D", "D", "D", "D", "A"}
	};
	
	static String[][] board = {
		{"A", "D", "D", "D", "D", "D", "D", "D", "D", "D"},
		{"A", "D", "D", "D", "D", "D", "D", "D", "D", "D"},
		{"D", "D", "D", "A", "D", "D", "D", "D", "D", "D"},
		{"D", "D", "D", "D", "A", "D", "D", "D", "D", "D"},
		{"D", "D", "A", "D", "D", "A", "D", "D", "D", "A"},
		{"D", "A", "D", "A", "A", "D", "D", "A", "D", "D"},
		{"D", "D", "A", "D", "D", "D", "D", "D", "A", "A"},
		{"D", "A", "D", "D", "D", "D", "D", "D", "D", "A"},
		{"A", "D", "D", "D", "D", "D", "D", "D", "D", "A"},
		{"D", "D", "D", "D", "D", "D", "D", "D", "D", "A"}
	};
	
	static String[][] newBoard = new String[10][10];
	
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			System.out.print("Enter the input: ");
			input = new Scanner(System.in);
			String inputStr = input.next();
			String[] inputArr = inputStr.split(",");
			int[] numArr = new int[inputArr.length];
			for(int j = 0; j < inputArr.length; j++) {
				numArr[j] = Integer.parseInt(inputArr[j]);
			}
			board = original;
			int coord1 = numArr[numArr.length - 2];
			int coord2 = numArr[numArr.length - 1];
			String output = status(coord1, coord2);
			for(int k = 0; k < numArr[numArr.length - 3]; k++) {
				runRules(numArr);
				output += status(coord1, coord2);
			}
			System.out.println(output);
		}
		
	}
	
	public static void runRules(int[] numArr) {
		int[] birthWays = new int[numArr[0]];
		for(int i = 0; i < birthWays.length; i++) {
			birthWays[i] = numArr[i + 1];
		}
		
		int[] surviveWays = new int[numArr.length - numArr[0] - 5];
		for(int j = 0; j < surviveWays.length; j++) {
			surviveWays[j] = numArr[j + numArr[0] + 2];
		}
		
		int numNeigh = 0;
		for(int a = 0; a < board.length; a++) {
			for(int b = 0; b < board[a].length; b++) {
				numNeigh = numNeighAlive(a + 1, b + 1);
				if(board[a][b] == "A") {
					boolean doesSurvive = false;
					for(int c = 0; c < surviveWays.length; c++) {
						if(numNeigh == surviveWays[c]) {
							doesSurvive = true;
						}
					}
					if(doesSurvive != true) {
						newBoard[a][b] = "D";
					} else {
						newBoard[a][b] = "A";
					}
				} else if(board[a][b] == "D") {
					boolean doesBirth = false;
					for(int d = 0; d < birthWays.length; d++) {
						if(numNeigh == birthWays[d]) {
							doesBirth = true;
						}
					}
					if(doesBirth) {
						newBoard[a][b] = "A";
					} else {
						newBoard[a][b] = "D";
					}
				}
			}
		}
		board = (String[][])newBoard.clone();
		newBoard = new String[10][10];
	}
	
	public static boolean isCell(int coord1, int coord2) {
		if(coord1 >= 1 && coord1 <= 10) {
			if(coord2 >= 1 && coord2 <= 10) {
				return true;
			}
		}
		
		return false;
	}
	
	public static String status(int coord1, int coord2) {
		String output = board[coord1 - 1][coord2 - 1];
		return output;
	}
	
	public static int numNeighAlive(int coord1, int coord2) {
		int numAlive = 0;
		if(isCell(coord1 - 1, coord2 - 1) && status(coord1 - 1, coord2 - 1) == "A") {
			numAlive++;
		}
		if(isCell(coord1 - 1, coord2) && status(coord1 - 1, coord2) == "A") {
			numAlive++;
		}
		if(isCell(coord1 - 1, coord2 + 1) && status(coord1 - 1, coord2 + 1) == "A") {
			numAlive++;
		}
		if(isCell(coord1, coord2 - 1) && status(coord1, coord2 - 1) == "A") {
			numAlive++;
		}
		if(isCell(coord1, coord2 + 1) && status(coord1, coord2 + 1) == "A") {
			numAlive++;
		}
		if(isCell(coord1 + 1, coord2 - 1) && status(coord1 + 1, coord2 - 1) == "A") {
			numAlive++;
		}
		if(isCell(coord1 + 1, coord2) && status(coord1 + 1, coord2) == "A") {
			numAlive++;
		}
		if(isCell(coord1 + 1, coord2 + 1) && status(coord1 + 1, coord2 + 1) == "A") {
			numAlive++;
		}
		return numAlive;
	}
}

