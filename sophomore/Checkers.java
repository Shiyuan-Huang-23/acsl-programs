import java.util.Scanner;

public class Checkers {
	static int[] yourChecker = new int[2];
	static int checkerNumber = 0;
	static String oppChecker = "";
	
	public static void main(String[] args) {
		oppChecker = "";
		Scanner input;
		for(int i = 0; i < 5; i++) {
			System.out.print("Please enter the inputs: ");
			input = new Scanner(System.in);
			String[] inputArr = input.next().split(",");
			int[] intArr = new int[inputArr.length];
			for(int j = 0; j < inputArr.length; j++) {
				intArr[j] = Integer.parseInt(inputArr[j]);
			}
			
			yourChecker[0] = intArr[0];
			yourChecker[1] = intArr[1];
			checkerNumber = intArr[2];
			
			StringBuilder sb = new StringBuilder(intArr.length - 3);
			for(int j = 3; j < intArr.length; j++) {
				sb.append(intArr[j]);
			}
			oppChecker = sb.toString();
			
		}
	}
	public static int moveCalc() {
		int moveNum = 0;
		return moveNum;
	}
}
