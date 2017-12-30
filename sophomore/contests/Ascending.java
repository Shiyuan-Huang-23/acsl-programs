import java.util.*;

public class Ascending {
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			System.out.print("Enter the input: ");
			input = new Scanner(System.in);
			String inputStr = input.nextLine();
			System.out.println(calcAscend(inputStr));
		}
	}
	
	public static String calcAscend(String inputStr) {
		String currentStr = "";
		String outputStr = "";
		//Find the first digit d
		int startNum = Integer.parseInt(inputStr.substring(0, 1));
		currentStr = inputStr.substring(1);
		//Find the first number
		int compareInt = 0;
		
		if(startNum != 0) {
			if(startNum <= currentStr.length()) {
				compareInt = Integer.parseInt(currentStr.substring(0, startNum));
				outputStr = outputStr + Integer.toString(compareInt);
				currentStr = currentStr.substring(startNum, currentStr.length());
			} else {
				return "";
			}
		}
		
		//Reverse the remaining string
		currentStr = new StringBuilder(currentStr).reverse().toString();
		//Loop through the remaining string to output ascending numbers
		int endIndex = 1;
		while(endIndex <= currentStr.length()) {
			int tempInt = Integer.parseInt(currentStr.substring(0, endIndex));
			if(tempInt <= compareInt) {
				endIndex = endIndex + 1;
			} else {
				outputStr = outputStr + " " + Integer.toString(tempInt);
				currentStr = currentStr.substring(endIndex, currentStr.length());
				compareInt = tempInt;
			}
		}
		return outputStr;
	}
}
