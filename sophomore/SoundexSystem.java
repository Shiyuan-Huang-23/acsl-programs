import java.util.*;

public class SoundexSystem {
	
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			System.out.print("Enter the input: ");
			input = new Scanner(System.in);
			String inputStr = input.nextLine();
			if(inputStr.contains(" ")) {
				String[] inputArr = inputStr.split(" ");
				System.out.print(soundexCode(inputArr[0] + inputArr[1]));
				System.out.print(" and ");
				System.out.println(soundexCode(inputArr[1]));
			} else {
				System.out.println(soundexCode(inputStr));
			}
		}
	}
	public static String soundexCode(String lastName) {
		String[] soundexParts = new String[4];
		List<Integer> numParts = new ArrayList<Integer>();
		soundexParts[0] = lastName.substring(0, 1);
		//Find the corresponding numbers for the letters
		for(int i = 0; i < lastName.length(); i++) {
			numParts.add(letterToNum(lastName.substring(i, i + 1)));
		}
		//Consonant separators
		Iterator<Integer> itera = numParts.iterator();
		int currentIndex = 0;
		while(itera.hasNext()) {
			int currentInt = itera.next();
			if(currentIndex + 2 < numParts.size()) {
				int firstInt = numParts.get(currentIndex + 1);
				int secondInt = numParts.get(currentIndex + 2);
				if(firstInt == 0 && currentInt == secondInt) {
					itera.remove();
				}
				currentIndex++;
				if(currentIndex + 2 < numParts.size()) {
					firstInt = numParts.get(currentIndex + 1);
					secondInt = numParts.get(currentIndex + 2);
				}
			}
		}
		//Remove duplicate sounds
		Iterator<Integer> iter = numParts.iterator();
		int compareInt = numParts.get(0);
		while(iter.hasNext()) {
			int currentInt = iter.next();
			if(currentInt == compareInt) {
				iter.remove();
			} else {
				compareInt = currentInt;
			}
		}
		//Remove -1 and 0
		Iterator<Integer> newIter = numParts.iterator();
		while(newIter.hasNext()) {
			int currentInt = newIter.next();
			if(currentInt == -1 || currentInt == 0) {
				newIter.remove();
			}
		}
		//Adds numbers to the code
		int index = 0;
		Iterator<Integer> newIter2 = numParts.iterator();
		while(newIter2.hasNext()) {
			int currentInt = newIter2.next();
			if((index + 1) < soundexParts.length) {
				soundexParts[index + 1] = Integer.toString(currentInt);
				index = index + 1;
			}
		}
		//Adds extra zeros
		for(int i = 0; i < soundexParts.length; i++) {
			if(soundexParts[i] == null) {
				soundexParts[i] = "0";
			}
		}
		String finalString = "";
		for(int i = 0; i < soundexParts.length; i++) {
			finalString = finalString + soundexParts[i];
		}
		return finalString;
	}
	
	public static int letterToNum(String letter) {
		//This converts a letter to its corresponding number
		//If it is one of the ignored letters, then it returns -1
		if(letter.equals("B") || letter.equals("F") || letter.equals("P") || letter.equals("V")) {
			return 1;
		} else if(letter.equals("C") || letter.equals("G") || letter.equals("J") || letter.equals("K")
				|| letter.equals("Q") || letter.equals("S") || letter.equals("X") || letter.equals("Z")) {
			return 2;
		} else if(letter.equals("D") || letter.equals("T")) {
			return 3;
		} else if(letter.equals("L")) {
			return 4;
		} else if(letter.equals("M") || letter.equals("N")) {
			return 5;
		} else if(letter.equals("R")) {
			return 6;
		} else if(letter.equals("H") || letter.equals("W")) {
			return 0;
		} else {
			return -1;
		}
	}
}




