import java.util.*;

//(ADD (EXP -3 2) (SQR 5) (SUB 6 2) (MULT 6 7 -2 3) (DIV 15 5))

public class LispExpressions {

    public static String[] sublists;

    public static void main(String[] args) {
        for(int i = 0; i < 6; i++) {
            Scanner in = new Scanner(System.in);
            System.out.print("Enter the input: ");
            String input = in.nextLine();
            if(i == 0) {
                sublists = findSublists(input);
            } else {
                if(input.equals("COUNT")) {
                    int n = 0;
                    for(int j = 0; j < sublists.length; j++) {
                        if(isSublist(sublists[j])) {
                            n++;
                        }
                    }
                    System.out.println(n);
                } else if(input.equals("MAXIMUM")) {
                    int maxIndex = 0;
                    int maxSpaces = 0;
                    for(int j = 0; j < sublists.length; j++) {
                        if(isSublist(sublists[j])) {
                            int spaces = sublists[j].split(" ").length;
                            if(spaces > maxSpaces) {
                                maxSpaces = spaces;
                                maxIndex = j;
                            }
                        }
                    }
                    System.out.println(sublists[maxIndex]);
                } else if(input.indexOf("REMOVE") != -1) {
                    String[] arguments = input.split(" ");
                    int start = Integer.parseInt(arguments[1]);
                    int end = Integer.parseInt(arguments[2]);
                    int sublistNumber = 0;
                    String lastPrinted = "";

                    for(int j = 0; j < sublists.length; j++) {
                        if(isSublist(sublists[j])) {
                            sublistNumber++;
                            if(sublistNumber < start || sublistNumber > end) {
                                System.out.print(sublists[j]);
                                lastPrinted = sublists[j];
                            }
                        } else {
                            if(!sublists[j].equals(" ") || !lastPrinted.equals(" ")) {
                                System.out.print(sublists[j]);
                                lastPrinted = sublists[j];
                            }
                        }
                    }
                    System.out.println();
                } else if(input.indexOf("REVERSE") != -1) {
                    String[] arguments = input.split(" ");
                    int start = Integer.parseInt(arguments[1]);
                    int end = Integer.parseInt(arguments[2]);
                    int sublistNumber = 0;
                    int startIndex = -1;
                    int endIndex = -1;
                    String[] targetSublists = new String[end - start + 1];

                    //Find indices of corresponding sublists
                    for(int j = 0; j < sublists.length; j++) {
                        if(isSublist(sublists[j])) {
                            sublistNumber++;
                            if(sublistNumber == start) {
                                startIndex = j;
                            }
                            if(sublistNumber == end) {
                                endIndex = j;
                            }
                            if(sublistNumber >= start && sublistNumber <= end) {
                                targetSublists[sublistNumber - start] = sublists[j];
                            }
                        }
                    }

                    for(int j = 0; j < targetSublists.length; j++) {
                        String[] elements = targetSublists[j].substring(1, targetSublists[j].length() - 1).split(" ");
                        for(int k = 1; k < (elements.length + 1) / 2; k++) {
                            String temp = elements[k];
                            elements[k] = elements[elements.length - k];
                            elements[elements.length - k] = temp;
                        }
                        String output = Arrays.toString(elements).replace(", ", " ");
                        output = output.substring(1, output.length() - 1);
                        targetSublists[j] = "(" + output + ")";
                    }

                    for(int j = 0; j < targetSublists.length / 2; j++) {
                        String temp = targetSublists[j];
                        targetSublists[j] = targetSublists[targetSublists.length - j - 1];
                        targetSublists[targetSublists.length - j - 1] = temp;
                    }

                    for(int j = 0; j < startIndex; j++) {
                        System.out.print(sublists[j]);
                    }

                    String output = Arrays.toString(targetSublists).replace(", ", " ");
                    output = output.substring(1, output.length() - 1);
                    System.out.print(output);
                    for(int j = endIndex + 1; j < sublists.length; j++) {
                        System.out.print(sublists[j]);
                    }

                    System.out.println();
                } else if(input.indexOf("SORT") != -1) {
                    String[] arguments = input.split(" ");
                    int start = Integer.parseInt(arguments[1]);
                    int end = Integer.parseInt(arguments[2]);
                    int sublistNumber = 0;
                    int startIndex = -1;
                    int endIndex = -1;
                    String[] targetSublists = new String[end - start + 1];

                    for(int j = 0; j < sublists.length; j++) {
                        if(isSublist(sublists[j])) {
                            sublistNumber++;
                            if(sublistNumber == start) {
                                startIndex = j;
                            }
                            if(sublistNumber == end) {
                                endIndex = j;
                            }

                            if(sublistNumber >= start && sublistNumber <= end) {
                                targetSublists[sublistNumber - start] = sublists[j];
                            }
                        }
                    }

                    Arrays.sort(targetSublists);

                    for(int j = 0; j < startIndex; j++) {
                        System.out.print(sublists[j]);
                    }

                    String output = Arrays.toString(targetSublists).replace(", ", " ");
                    output = output.substring(1, output.length() - 1);
                    System.out.print(output);
                    for(int j = endIndex + 1; j < sublists.length; j++) {
                        System.out.print(sublists[j]);
                    }
                    System.out.println();
                }
            }
        }
    }

    public static String[] findSublists(String input) {
        String output = "";
        String temp = "";
        int openIndex;
        int closeIndex;

        for(int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            openIndex = input.indexOf("(", i);
            closeIndex = input.indexOf(")", i);

            if(c == '(') {
                if(temp.length() == 0) {
                    temp = "(";
                } else {
                    temp += ":";
                    output += temp;
                    temp = "(";
                }
            } else if(c == ')') {
                temp += "):";
                output += temp;
                temp = "";
            } else {
                temp += String.valueOf(c);
            }
        }

        String[] outputArr = output.split(":");
        return outputArr;
    }

    public static boolean isSublist(String input) {
        if(input.indexOf("(") != -1 && input.indexOf(")") != -1) {
            return true;
        }
        return false;
    }
}
