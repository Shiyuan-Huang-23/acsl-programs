/*
Sample Inputs
8, 9, Q, 6, 7, K, A, 5, 9, 8
75, J, 7, Q, T, A, 6, 2, 3, 4, 5
50, 7, K, T, 8, 3, Q, 9, 7, 2, 3
63, 3, 6, 8, T, 7, 7, T, 3, 5, 8
79, A, 9, 7, T, A, 9, T, A, 6, 4
50, A, T, Q, A, T, K, J, T, A, 7
*/

package junior;
import java.util.Arrays;
import java.util.Scanner;

public class ACSLNinetyNine {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		//Obtain 6 lines of input
		String[] hand1 = new String[5];
		String[] hand2 = new String[5];
		for(int i = 0; i < 6; i++) {
			if(i == 0) {
				System.out.print("Enter the cards: ");
				//Get the starting two hands from first deck
				String[] hands = in.nextLine().split(", ");
				hand1 = Arrays.copyOfRange(hands, 0, 5);
				hand2 = Arrays.copyOfRange(hands, 5, 10);
			} else {
				System.out.print("Enter input: ");
				String[] refills = in.nextLine().split(", ");
				simulate(refills, hand1, hand2);
			}
		}
		in.close();
	}
	
	public static void simulate(String[] refills, String[] hand1, String[] hand2) {
		//Obtain starting point value
		int points = Integer.parseInt(refills[0]);
		//Convert String[] hands into int[]
		int[] localHand1 = convert(hand1);
		int[] localHand2 = convert(hand2);
		for(int i = 1; i < refills.length; i += 2) {
			//Sort hands according to point value
			sortHand(localHand1);
			//Play the median card + handle irregularities, returns points
			points = playCards(localHand1, points);
			//Replaces the used up median card with a refill
			localHand1[2] = valueOf(refills[i]);
			if(points > 99) {
				System.out.println(points + ", Player #2");
				break;
			}
			
			//Same process with Player 2
			sortHand(localHand2);
			points = playCards(localHand2, points);
			localHand2[2] = valueOf(refills[i + 1]);
			
			//If over 99, return points and winner's number
			if(points > 99) {
				System.out.println(points + ", Player #1");
				break;
			}
		} 
		//Play one last round without refilling if not over 99
		if(points <= 99) {
			sortHand(localHand1);
			points = playCards(localHand1, points);
			if(points > 99) {
				System.out.println(points + ", Player #2");
			} else {
				sortHand(localHand2);
				points = playCards(localHand2, points);
				if(points > 99) {
					System.out.println(points + ", Player #1");
				}
			}
		}
	}
	
	public static int playCards(int[] hand, int points) {
		int value = hand[2];
		//Exceptions
		if(value == 9) {
			return points;
		} else {
			if(value == 10) {
				value *= -1;
			} else if(value == 7) {
				if(points + value > 99) {
					value = 1;
				}
			}
			points += crossBorder(points, value);
		}
		return points + value;
	}
	
	//Converts cards into an int[] with their corresponding values
	public static int[] convert(String[] hand) {
		int[] output = new int[hand.length];
		for(int i = 0; i < hand.length; i++) {
			output[i] = valueOf(hand[i]);
		}
		return output;
	}
	
	//Sorts the player's hand according to point value
	public static void sortHand(int[] hand) {
		for(int i = 1; i < hand.length; i++) {
			int temp = hand[i];
			int j = i - 1;
			while(j >= 0 && temp < hand[j]) {
				hand[j + 1] = hand[j];
				j--;
			}
			hand[j + 1] = temp;
		}
	}
	
	//Adds 5 when point total borders are crossed
	public static int crossBorder(int points, int value) {
		int output = 0;
		if(value != -10) {
			if(points <= 33 && points + value > 33) {
				output = 5;
			} else if(points <= 55 && points + value > 55) {
				output = 5;
			} else if(points <= 77 && points + value > 77) {
				output = 5;
			}
		} else {
			if(points >= 78 && points + value < 78) {
				output = 5;
			} else if(points >= 56 && points + value < 56) {
				output = 5;
			} else if(points >= 34 && points + value < 34) {
				output = 5;
			}
		}
		return output;
	}
	
	//Converts cards into their value
	public static int valueOf(String card) {
		int output = 0;
		if(card.equals("T"))
			output = 10;
		else if(card.equals("J"))
			output = 11;
		else if(card.equals("Q"))
			output = 12;
		else if(card.equals("K"))
			output = 13;
		else if(card.equals("A"))
			output = 14;
		else
			output = Integer.parseInt(card);
		return output;
	}
	
	public static void display(String[] array) {
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}
		System.out.println();
	}
	
	public static void display(int[] array) {
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}
		System.out.println();
	}
}
