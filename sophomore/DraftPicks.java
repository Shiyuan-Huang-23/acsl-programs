import java.util.Scanner;

public class DraftPicks {
	static double[] stats = new double[20];
	public static void main(String[] args) {
		Scanner input;
		for(int i = 0; i < 20; i = i + 2) {
			input = new Scanner(System.in);
			System.out.print("Enter the next line of input: ");
			String inputStr = input.nextLine();
			inputStr = inputStr.replaceAll("\\s", "");
			String [] inputArr = inputStr.split(",");
			stats[i] = Double.parseDouble(inputArr[0]);
			stats[i + 1] = Double.parseDouble(inputArr[1]);
		}
		calcAvg();
		largestSal();
		ranges();
		diff();
	}
	
	public static void calcAvg() {
		double sum = 0;
		for(int i = 0; i < 20; i = i + 2) {
			double currentAvg = stats[i + 1] / stats[i];
			sum += currentAvg;
		}
		int average = (int) Math.round(sum * 100000);
		System.out.println(average);
	}
	
	public static void largestSal() {
		double largestAvg = 0;
		int largestPick = 0;
		for(int i = 0; i < 20; i = i + 2) {
			double currentAvg = stats[i + 1] / stats[i];
			if(currentAvg > largestAvg) {
				largestAvg = currentAvg;
				largestPick = (i + 2) / 2;
			}
		}
		largestAvg = largestAvg * 1000000;
		System.out.println((int) Math.round(largestAvg) + " by #" + largestPick);
	}
	
	public static void ranges() {
		double maxSalary = stats[1] / stats[0] /16;
		double minSalary = maxSalary;
		for(int i = 0; i < 20; i = i + 2) {
			double currentSalary = stats[i + 1] / stats[i] / 16;
			if(currentSalary > maxSalary) {
				maxSalary = currentSalary;
			} else if (currentSalary < minSalary) {
				minSalary = currentSalary;
			}
		}
		int range = (int) Math.round((maxSalary - minSalary) * 1000000);
		System.out.println(range);
		double newMaxSal = maxSalary * 8 / 9;
		double newMinSal = minSalary * 8 / 9;
		int midrange = (int) Math.round(((newMaxSal + newMinSal) / 2) * 1000000);
		System.out.println(midrange);
	}
	
	public static void diff() {
		double sum = 0;
		for(int i = 0; i < 20; i = i + 2) {
			double currentAvg = stats[i + 1] / stats[i];
			sum += currentAvg;
		}
		double average = sum / 10;
		double pay16 = average / 16 * 1000000;
		double pay18 = average / 18 * 1000000;
		System.out.println((int) Math.round(pay16 - pay18));
		
	}
	
}

