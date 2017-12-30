import java.util.Scanner;

public class BridgePoints {	
	static boolean vulnerable1 = false;
    static boolean vulnerable2 = false;
    static int below1 = 0;
    static int above1 = 0;
    static int below2 = 0;
    static int above2 = 0;
    static int teamNum;
    static int bids;
    static int tricksWon;
    static String suit;
    
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 5; i++) {
			System.out.print("Enter the inputs separated by commas: ");
			input = new Scanner(System.in);
			String inputStr = input.next();
			String[] inputArr = inputStr.split(",");
			teamNum = Integer.parseInt(inputArr[0]);
			bids = Integer.parseInt(inputArr[1]);
            tricksWon = Integer.parseInt(inputArr[2]);        
            suit = inputArr[3];
            calcPoints();
            System.out.println("The output is: " + below1 + "," + above1 + "," + below2 + "," + above2);
            if(below1 >= 100 || below2 >= 100) {
                below1 = 0;
                below2 = 0;
            }
		}
	}
	
	public static int[] calcPoints(){
		if(tricksWon >= bids + 6) {
            if(teamNum == 1) {
                vulnerable1 = true;
            } else {
                vulnerable2 = true;
            }
        }
		
		if(tricksWon >= bids + 6) {
            if(suit.equals("H") || suit.equals("S")) {
                if(teamNum == 1) {
                    below1 += bids * 30;
                    above1 += (tricksWon - (bids + 6)) * 30;
                } else {
                    below2 += bids * 30;
                    above2 += (tricksWon - (bids + 6)) * 30;
                }
            } else if(suit.equals("C") || suit.equals("D")) {
                if(teamNum == 1) {
                    below1 += bids * 20;
                    above1 += (tricksWon - (bids + 6)) * 20;
                } else {
                    below2 += bids * 20;
                    below1 += (tricksWon - (bids + 6)) * 20;
                }
            } else {
                if(teamNum == 1) {
                    below1 += 40 + (bids - 1) * 30;
                    above1 += (tricksWon - (bids + 6)) * 30;
                } else {
                    below2 += 40 + (bids - 1) * 30;
                    above2 += (tricksWon - (bids + 6)) * 30;
                }
            }
        }
		
		if(tricksWon < bids + 6) {
            if(teamNum == 1) {
                if(vulnerable1 == true) {               
                    above2 += 100 * (bids + 6 - tricksWon);
                } else {                    
                    above2 += 50 * (bids + 6 - tricksWon);
                }
            } else {
                if(vulnerable2 == true) {
                    above1 += 100 * (bids + 6 - tricksWon);
                } else {
                    above1 += 50 * (bids + 6 - tricksWon);
                }
            }
        }
        int[] output = {below1, above1, below2, above2};
        below1 = output[0];
        above1 = output[1];
        below2 = output[2];
        above2 = output[3];
        return output;
		
	}
}
