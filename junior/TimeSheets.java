import java.util.*;
import java.io.*;


public class TimeSheets {
	public static void main (String[] args) {
		//Using Scanner to input data
		//scan();
		//Using text file to input data
		getFile();
	}
	
	public static void getFile() {
		Scanner input = new Scanner(System.in);
		System.out.print("File name: ");
		
		//Tries to display file
		try {
			String filename = input.next();
			System.out.println();
			fileInput(filename);
		}
		//Displays errors
		catch(FileNotFoundException e) {
			System.out.println(e);
		}
		catch(IOException e) {
			System.out.println(e);
		}
		
		input.close();
	}
	
	public static void fileInput(String filename) throws IOException, FileNotFoundException {
		int c;
		//Create File object
		File input = new File(filename);
		
		//Connect to stream
		FileInputStream in = new FileInputStream(input);
		
		String data = "";
		
		//Read in chars
		while((c = in.read()) != -1) {
			//System.out.print((char) c);
			//System.out.print(" = " + c + "; ");
			//If there is a newline, run methods
			if(c == 13) {
				System.out.println("The data is " + data);
				String[] inArr = data.split(", ");
				double[] hours = hours(inArr);
				System.out.printf("$%.2f%n", pay(hours));
				System.out.println("");
				data = "";
			} else {
			//Keep reading otherwise, disregard newline chars
				if(c != 10) {
					data += String.valueOf((char) c);
				}
			}
		}
		//If there is still data not ending in /n, process it
		if(!data.equals("")) {
			System.out.println("The data is " + data);
			String[] inArr = data.split(", ");
			double[] hours = hours(inArr);
			System.out.printf("$%.2f%n", pay(hours));
			System.out.println("");
			data = "";
		}
		System.out.println();
		
		//Close input stream
		in.close();
	}
	 
	public static void scan() {
		Scanner in = new Scanner(System.in);
		for(int i = 0; i < 5; i++) {
			System.out.println("Input, different days separated by commas and spaces, hours on the same day separated by commas: ");
			String[] input = in.nextLine().split(", ");
			double[] hours = hours(input);
			System.out.printf("$%.2f%n", pay(hours));
			System.out.println("");
		}
		in.close();
	}
	
	//Converts input into an array of hours worked per day
	public static double[] hours(String[] input) {
		double[] hours = new double[8];
		for(int i = 0; i < input.length; i++) {
			if(i == 0) {
				hours[i] = (double) Integer.parseInt(input[i]);
			} else {
				int begin = charToNum(input[i].charAt(0));
				int end = charToNum(input[i].charAt(2));
				hours[i] = 0.5 * (end - begin);
			}
		}
		return hours;
	}
	  
	//Turns a int or char to its corresponding time, with 9:00 being 1
	public static int charToNum(int a) {
		if(a >= 49 && a <= 57) {
			//Converts ASCII for numbers 1-9
			return a - 48;
		} else {
			//Converts A-H
			return a - 55;
		}
	}
	  
	//Calculates pay based on hours
	public static double pay(double[] hours) {
		double wage = 0;
		if((int) hours[0] / 100 == 4) {
			wage += 13.5 * (hours[1] + hours[7]);
			double otherHours = 0;
			for(int i = 2; i < 7; i++) {
				otherHours += hours[i];
			}
			wage += 6.75 * otherHours;
			return wage;
		} else if((int) hours[0] / 100 == 5) {
			for(int i = 1; i < hours.length; i++) {
				if(hours[i] > 6) {
					wage += 12 * (hours[i] - 6);
					hours[i] = 6;
				}
				wage += 8 * hours[i];
			}
			return wage;
		}
		  
		double totalHours = 0;
		for(int i = 1; i < hours.length; i++) {
			totalHours += hours[i];
		}
		  
		if((int) hours[0] / 100 == 1) {
			if(totalHours > 30) {
				wage += 15.0 * (totalHours - 30);
				totalHours = 30;
			}
			wage += 10.0 * totalHours;
			return wage;
		} else if((int) hours[0] / 100 == 2) {
			if(totalHours > 40) {
				wage += 15.0 * (totalHours - 40);
				totalHours = 40;
			}
			wage += 7.5 * totalHours;
			return wage;
		} else {
			if(totalHours > 20) {
				wage += 10.5 * (totalHours - 20);
				totalHours = 20;
			}
			wage += 9.25 * totalHours;
			return wage;
		}
	}
}
