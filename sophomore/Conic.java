import java.util.*;

public class Conic {
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			input = new Scanner(System.in);
			System.out.print("Enter the input: ");
			String inputStr = input.nextLine();
			if(inputStr.contains("xy")) {
				System.out.println("Neither");
			} else {
				int[] coefficients = findCoef(findTerms(inputStr));
				String circOEclip = circEclip(coefficients);
				System.out.print(circOEclip + ", ");
				int[] completed = findCenter(coefficients);
				System.out.print("(" + completed[2] + ", " + completed[3] + ")" );
				System.out.print(", " + findAxis(circOEclip, completed) + "\n");
			}
		}
	}
	
	public static int findAxis(String circOEclip, int[] input) {
		if(circOEclip.contains("Ellipse")) {
			int firstFrac = input[4] / input[0];
			int secondFrac = input[4] / input[1];
			if(firstFrac >= secondFrac) {
				double axis = (2 * java.lang.Math.pow((double) firstFrac, 0.5));
				int newAxis = (int) axis;
				return newAxis;
			} else {
				double axis = (2 * java.lang.Math.pow((double) secondFrac, 0.5));
				int newAxis = (int) axis;
				return newAxis;
			}
		} else {
			double radius = java.lang.Math.pow((double) input[4], 0.5);
			int newRadius = (int) radius;
			return newRadius;
		}
	}
	
	public static int[] findCenter(int[] input) {
		int[] output = new int[5];
		//Move constant to right side of equation
		input[4] = -1 * input[4]; 
		int x2Coef = input[0];
		int y2Coef = input[1];
		//Divide by the coefficient of x^2
		if(x2Coef != 1) {
			input[0] = 1;
			input[2] = input[2] / x2Coef;
		}
		//Divide by the coefficient of y^2
		if(y2Coef != 1) {
			input[1] = 1;
			input[3] = input[3] / y2Coef;
		}
		//Complete the square for x and y
		int temp = input[2] / 2;
		input[4] = input[4] + (x2Coef * temp * temp);
		temp = input[3] / 2;
		input[4] = input[4] + (y2Coef * temp * temp);
		/* 
		 * Index 0 contains x2Coef
		 * Index 1 contains y2Coef
		 * Index 2 contains the x coordinate of center
		 * Index 3 contains the y coordinate of center
		 * Index 4 contains input[4]
		*/
		output[0] = x2Coef;
		output[1] = y2Coef;
		output[2] = input[2] / -2;
		output[3] = input[3] / -2;
		output[4] = input[4];
		return output;
	}
	
	public static String circEclip(int[] input) {
		if(input[0] == input[1]) {
			return "Circle";
		} else {
			return "Ellipse";
		}
	}
	public static String[] findTerms(String input) {
		String[] terms = new String[5];
		int index = 0;
		index = input.indexOf("x^2");
		terms[0] = input.substring(0, index + 3);
		input = input.substring(index + 3);
		index = input.indexOf("y^2");
		terms[1] = input.substring(0, index + 3);
		input = input.substring(index + 3);
		if(input.contains("x")) {
			index = input.indexOf("x");
			terms[2] = input.substring(0, index + 1);
			input = input.substring(index + 1);
		}
		if(input.contains("y")) {
			index = input.indexOf("y");
			terms[3] = input.substring(0, index + 1);
			input = input.substring(index + 1);
		}
		index = input.indexOf("=");
		if(input.substring(0, index).length() != 0) {
			terms[4] = input.substring(0, index);
		}
		return terms;
	}
	
	public static int[] findCoef(String[] input) {
		int[] coefficients = new int[5];
		int index = 0;
		index = input[0].indexOf("x^2");
		String sub = input[0].substring(0, index);
		if(sub.length() == 0) {
			coefficients[0] = 1;
		} else if(sub.length() == 1 && sub.contains("-")) {
			coefficients[0] = -1;
		} else {
			coefficients[0] = Integer.parseInt(input[0].substring(0, index));
		}
		index = input[1].indexOf("y^2");
		sub = input[1].substring(0, index);
		if(sub.length() == 1 && sub.contains("+")) {
			coefficients[1] = 1;
		} else if(sub.length() == 1 && sub.contains("-")) {
			coefficients[1] = -1;
		} else {
			coefficients[1] = Integer.parseInt(sub);
		}
		if(input[2] != null) {
			index = input[2].indexOf("x");
			sub = input[2].substring(0, index);
			if(sub.length() == 1 && sub.contains("+")) {
				coefficients[2] = 1;
			} else if(sub.length() == 1 && sub.contains("-")) {
				coefficients[2] = -1;
			} else {
				coefficients[2] = Integer.parseInt(sub);
			}
		}
		if(input[3] != null) {
			index = input[3].indexOf("y");
			sub = input[3].substring(0, index);
			if(sub.length() == 1 && sub.contains("+")) {
				coefficients[3] = 1;
			} else if(sub.length() == 1 && sub.contains("-")) {
				coefficients[3] = -1;
			} else {
				coefficients[3] = Integer.parseInt(sub);
			}
		}
		if(input[4] != null) {
			coefficients[4] = Integer.parseInt(input[4]);
		}
		return coefficients;
	}
}
