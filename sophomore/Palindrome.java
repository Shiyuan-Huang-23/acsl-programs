import java.util.*;

public class Palindrome {
	
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			input = new Scanner(System.in);
			System.out.print("Enter the input: ");
			String inputStr = input.nextLine();
			String[] inputArr;
			if(inputStr.contains(", ")) {
				inputArr = inputStr.split(", ");
			} else {
				inputArr = inputStr.split(",");
			}
			if(inputArr[0].equals(reverse(inputArr[0]))) {
				System.out.println(inputArr[0]);
			} else {
				String outPalin = makePalin(inputArr[0], inputArr[1]);
				if(outPalin.equals(reverse(outPalin))) {
					System.out.println(outPalin);
				} else {
					System.out.println("NONE, " + outPalin);
				}
			}
		}
	}
	
	public static String makePalin(String num, String base) {
		int count = 0;
		String palindrome = "";
		String temp = num;
		while(true) {
			if(count == 10) {
				palindrome = temp;
				break;
			}
			count ++;
			temp = reverseAdd(temp, base);
			if(temp.equals(reverse(temp))) {
				palindrome = temp;
				break;
			}
		}
		return palindrome;
	}
	
	public static String reverseAdd(String num, String base) {
		int intBase = Integer.parseInt(base);
		int firstNum = Integer.parseInt(num, intBase);
		int secondNum = Integer.parseInt(reverse(num), intBase);
		int sum = firstNum + secondNum;
		String convert = convert(sum, intBase);
		return convert;
	}
	
	public static String reverse(String input) {
		char[] in = input.toCharArray();
	    int begin = 0;
	    int end = in.length-1;
	    char temp;
	    while(end > begin){
	        temp = in[begin];
	        in[begin] = in[end];
	        in[end] = temp;
	        end--;
	        begin++;
	    }
	    return new String(in);
	}
	
	public static String convert(int number, int base) {
	    int quotient = number / base;
	    int remainder = number % base;

	    if (quotient == 0) {
	        return Integer.toString(remainder);      
	    } else {
	        return convert(quotient, base) + Integer.toString(remainder);
	    }            
	}
}
