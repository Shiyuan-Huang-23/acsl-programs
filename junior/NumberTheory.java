import java.util.*;

public class NumberTheory
{
	public static void main (String[] args) 
	{
		//Input: 16, 5, 12, 15; Output: 61, 3, 15, 240, 1074, 17
		
		Scanner in = new Scanner(System.in);
		System.out.println("Enter 4 positive integers separated by commas and spaces: ");
		String input = in.nextLine();
		String[] inArr = input.split(", ");
		
		//Reverse A
		StringBuilder output1 = new StringBuilder();
		output1.append(inArr[0]);
		output1 = output1.reverse();
		for(int i = 0; i < output1.length(); i++) {
			System.out.print(output1.charAt(i));
		}
		System.out.println("");
		
		//Find largest quotient
		int[] intArr = new int[4];
		for(int i = 0; i < inArr.length; i++) {
			intArr[i] = Integer.parseInt(inArr[i]);
		}
		int min = intArr[0];
		int max = intArr[0];
		for(int i = 1; i < intArr.length; i++) {
			if(intArr[i] > max) {
				max = intArr[i];
			} else if(intArr[i] < min) {
				min = intArr[i];
			}
		}
		System.out.println(max / min);
		
		//Find largest remainder
		int remainder = intArr[0] % max;
		for(int i = 1; i < intArr.length; i++) {
			if(intArr[i] % max > remainder) {
				remainder = intArr[i] % max;
			}
		}
		System.out.println(remainder);
		
		//Find least common multiple
		int multiplier = 1;
		int temp = 0;
		boolean sentinel = true;
		while(sentinel) {
			temp = max * multiplier;
			for(int i = 0; i < intArr.length; i++) {
				if(temp % intArr[0] == 0) {
					if(temp % intArr[1] == 0) {
						if(temp % intArr[2] == 0) {
							if(temp % intArr[3] == 0) {
								sentinel = false;
							}
						}
					}
				}
			}
			multiplier++;
		}
		System.out.println(temp);
		
		//Find fibonacci number
		int a = intArr[0];
		int sum = intArr[0] + intArr[1] + intArr[2] + intArr[3];
		while(sum <= 1000) {
			intArr[0] = intArr[1];
			intArr[1] = intArr[2];
			intArr[2] = intArr[3];
			intArr[3] = sum;
			sum = intArr[0] + intArr[1] + intArr[2] + intArr[3];
		} 
		System.out.println(sum);
		
		//Find prime number
		boolean notFound = true;
		while(notFound) {
			a++;
			notFound = false;
			for(int i = 2; i < a/2; i++) {
				if(a % i == 0) {
					notFound = true;
				}
			}
		}
		System.out.println(a);
				
		in.close();
		
	}
}

