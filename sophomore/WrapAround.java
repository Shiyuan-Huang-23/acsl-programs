import java.util.*;

public class WrapAround {
	static final String[] ALPHABET = {"A", "B", "C", "D", 
		"E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
		"R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
	static final List<String> ALPHABETLIST = java.util.Arrays.asList(ALPHABET);
	static int startPlace = 1;
	
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			System.out.print("Enter the inputs: ");
			input = new Scanner(System.in);
			String inputStr = input.next();
			List<String> finalList = wrapCalc(inputStr.split(""));
			String output = String.join(" ", finalList);
			System.out.println(output);
			startPlace = 1;
		}
	}
	
	public static List<String> wrapCalc(String[] inputArray) {
		int newLetterVal = 0;
		String finalLetter = "";
		List<String> returnVal = new ArrayList<String>();
		
		for(int i = 0; i < inputArray.length; i++) {
			if(ALPHABETLIST.indexOf(inputArray[i]) != -1) {
				String letter = inputArray[i];
				int letterVal = ALPHABETLIST.indexOf(letter) + 1;
				if(letterVal <= 5) {
					newLetterVal = letterVal * 2;
				} else if (letterVal > 5 && letterVal <=10) {
					newLetterVal = (letterVal % 3) * 5;
				} else if (letterVal > 10 && letterVal <= 15) {
					newLetterVal = (int) (Math.floor(letterVal / 4) * 8) ;
				} else if (letterVal > 15 && letterVal <= 20) {
					newLetterVal = (int) (((letterVal % 10) + Math.floor (letterVal/10)) * 10);
				} else {
					newLetterVal = factorCalc(letterVal) * 12;
				} 
				newLetterVal += startPlace;
				//System.out.println("The new value of " + letter + " is " + newLetterVal);
				if(newLetterVal <= 26) {
					finalLetter = ALPHABET[newLetterVal - 1];
				} else if(newLetterVal % 26 == 0) {
					finalLetter = "Z";
				} else if(newLetterVal % 26 != 0 && newLetterVal > 26) {
					finalLetter = ALPHABET[(newLetterVal % 26) -1];
				}
				
				startPlace = ALPHABETLIST.indexOf(finalLetter) + 1;
				//System.out.println("The new starting place is " + startPlace);
				//System.out.println("The final letter is " + finalLetter);
				returnVal.add(finalLetter);
			}
		}
		
		return returnVal;
		
	}
	
	public static int factorCalc(int letterVal) {
		int maxFactor = 0;
		for(int i = 1; i < letterVal; i++) {
			if(letterVal % i == 0) {
				maxFactor = i;
			}
		}
		return maxFactor;
	}
}
