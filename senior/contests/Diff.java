import java.io.*;
import java.util.*;

public class Diff {
    public static void main(String[] args) {
        for(int i = 0; i < 5; i++) {
            Scanner input = new Scanner(System.in);
            System.out.print("Enter the first string: ");
            String strA = input.nextLine();
            System.out.print("Enter the second string: ");
            String strB = input.nextLine();

            String[] arrA = strA.split(" ");
            String copyB = strB;
            String commonStr1 = "";
            for(int j = 0; j < arrA.length; j++) {
                if(copyB.indexOf(arrA[j]) != -1) {
                    int wordIndex = copyB.indexOf(arrA[j]);
                    copyB = copyB.substring(0, wordIndex) + copyB.substring(wordIndex + arrA[j].length());
                    commonStr1 += arrA[j] + " ";
                }
            }
            commonStr1 = commonStr1.substring(0, commonStr1.length() - 1);

            String[] arrB = strB.split(" ");
            String copyA = strA;
            String commonStr2 = "";
            for(int j = 0; j < arrB.length; j++) {
                if(copyA.indexOf(arrB[j]) != -1) {
                    int wordIndex = copyA.indexOf(arrB[j]);
                    copyA = copyA.substring(0, wordIndex) + copyA.substring(wordIndex + arrB[j].length());
                    commonStr2 += arrB[j] + " ";
                }
            }
            commonStr2 = commonStr2.substring(0, commonStr2.length() - 1);

            String finalStr = "";
            String[] c = commonStr1.split("");
            for(int j = 1; j < c.length; j++) {
                if(!c[j].equals(" ")) {
                    if(commonStr2.indexOf(c[j]) != -1) {
                        finalStr += c[j];
                        commonStr2 = commonStr2.substring(commonStr2.indexOf(c[j]) + 1);
                    }
                }
            }
            if(finalStr.length() == 0) {
                System.out.println("NONE");
            } else {
                System.out.println(finalStr);
            }

        }
    }
}
