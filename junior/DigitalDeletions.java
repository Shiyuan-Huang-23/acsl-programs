import java.util.*;

public class DigitalDeletions {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        for(int j = 0; j < 5; j++) {
            System.out.print("Enter the numbers, separated by commas and spaces: ");

            //Obtain input and convert input into int array, cutting out the first value
            String[] strInput = in.nextLine().split(", ");
            int[] input = new int[strInput.length - 1];
            for(int i = 1; i < strInput.length; i++) {
                input[i - 1] = Integer.parseInt(strInput[i]);
            }

            //Count number of moves required
            System.out.println(count(input));
        }

    }

    //Finds the index of the last occurrence of the int n in the array a
    public static int lastOccur(int[] a, int n) {
        int output = -1;
        for(int i = 0; i < a.length; i++) {
            if(a[i] == n) {
                output = i;
            }
        }
        return output;
    }

    //Finds the median of an array
    public static int median(int[] a) {
        int median = 0;
        int[] b = Arrays.copyOf(a, a.length);
        Arrays.sort(b);
        if(b.length % 2 == 0) {
            int index1 = (b.length / 2) - 1;
            int index2 = b.length / 2;
            median = (int) (((double) b[index1] + b[index2]) / 2);
        } else {
            int index = (int) (b.length / 2);
            median = b[index];
        }
        return median;
    }

    //Removes rightmost zero and numbers to its left
    public static int[] cut(int[] a, int index) {
        int[] b = Arrays.copyOfRange(a, index + 1, a.length);
        return b;
    }

    //Counts number of moves
    public static int count(int[] input) {
        int moves = 0;
        while(input.length > 0) {
            //If there are zeros, get rid of them
            if(lastOccur(input, 0) != -1) {
                input = cut(input, lastOccur(input, 0));
                moves++;
            } else {
                //If there aren't zeros, calculate the median and decrement appropriate values accordingly
                int mid = median(input);
                int targetIndex = -1;

                //Find the value that needs to be decreased
                for(int i = mid; i > 0; i--) {
                    if(lastOccur(input, i) != -1) {
                        targetIndex = lastOccur(input, i);
                        break;
                    }
                }

                //Decrease the targeted value
                if(input[targetIndex] % 2 == 0) {
                    input[targetIndex] -= 2;
                } else {
                    input[targetIndex] -= 1;
                }
                moves++;
            }
        }
        return moves;
    }
}

