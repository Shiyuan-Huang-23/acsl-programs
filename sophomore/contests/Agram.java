/*
 * ACSL 2016-2017 Contest 1 Intermediate 
 * 12/05/2016
 * Shiyuan Huang
 * Grade 10
 * Barrington High School
 * Intermediate
 */


import java.util.Arrays;
import java.util.Scanner;

public class Agram {
	static String[] values = {"0", "1", "2", "3", "4", "5", "6", "7", "8", 
	"9", "T", "J", "Q", "K"};
	
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			System.out.print("Enter the input separated by commas: ");
			input = new Scanner(System.in);
			String inputStr = input.nextLine();
			String[] inputArr;
			if(inputStr.indexOf(", ") != -1) {
				inputArr = inputStr.split(", ");
			} else {
				inputArr = inputStr.split(",");
			}
			
			//System.out.println(Arrays.toString(inputArr));
			System.out.println(bestCard(inputArr));
		}
	}
	
	public static String bestCard(String[] inputArr) {
		String suit = inputArr[0].substring(1, 2);
		int cardValue = Arrays.asList(values).indexOf((inputArr[0].substring(0, 1)));
		
		boolean containsSuit = false;
		for(int i = 1; i < inputArr.length; i++) {
			if(inputArr[i].indexOf(suit) != -1) {
				containsSuit = true;
			} 
		}
		
		if(containsSuit == true) {
			String bestCard = null;
			int bestNum = 14;
			for(int i = 1; i < inputArr.length; i++) {
				if(inputArr[i].indexOf(suit) != -1) {
					if(findValue(inputArr[i]) > cardValue) {
						if(findValue(inputArr[i]) < bestNum) {
							bestNum = findValue(inputArr[i]);
							bestCard = inputArr[i];
						}
					}
				}
			}
			
			if(bestCard == null) {
				int smallestCard = 14;
				int index = 10;
				for(int i = 1; i < inputArr.length; i++) {
					if(inputArr[i].indexOf(suit) != -1) {
						if(findValue(inputArr[i]) < smallestCard) {
							smallestCard = findValue(inputArr[i]);
							index = i;
						}
					}
				}
				return inputArr[index];
			} else {
				return bestCard;
			}
			
		} else {
			int smallestCard = 14;
			int index = 10;
			for(int i = 1; i < inputArr.length; i++) {
				if(findValue(inputArr[i]) < smallestCard) {
					smallestCard = findValue(inputArr[i]);
					index = i;
				}
			}
			return inputArr[index];
		}
		
	}
	
	public static int findValue(String input) {
		input = input.substring(0, 1);
		return Arrays.asList(values).indexOf(input);
	}
}
