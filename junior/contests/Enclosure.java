import java.util.*;
import java.lang.*;

public class Enclosure {

    public static final String[] operations = {"+", "-", "*", "/"};

    public static void main(String[] args) {
        for(int i = 0; i < 1; i++) {
            ArrayList<String> enclosuresList = new ArrayList<String>(Arrays.asList("{", "[", "(", ")", "]", "}"));
            Scanner in = new Scanner(System.in);
            System.out.print("Enter the mathematical expression without any spaces: ");
            String expression = in.nextLine();
            // update enclosures to reflect enclosures in the expression
            if(expression.indexOf("{") < 0 && expression.indexOf("}") < 0) {
                enclosuresList.remove("{");
                enclosuresList.remove("}");
            }
            if(expression.indexOf("[") < 0 && expression.indexOf("]") < 0) {
                enclosuresList.remove("[");
                enclosuresList.remove("]");
            }
            if(expression.indexOf("(") < 0 && expression.indexOf(")") < 0) {
                enclosuresList.remove("(");
                enclosuresList.remove(")");
            }
            String[] enclosures = new String[enclosuresList.size()];
            enclosures = enclosuresList.toArray(enclosures);

            // fill enclosureIndices with the indices of the symbols in enclosures
            String missingSymbol = "";
            int missingSymbolIndex = -1;
            int[] enclosureIndices = new int[enclosures.length];
            for(int j = 0; j < enclosures.length; j++) {
                enclosureIndices[j] = expression.indexOf(enclosures[j]);
                if(enclosureIndices[j] == -1) {
                    missingSymbol = enclosures[j];
                    missingSymbolIndex = j;
                }
            }

            ArrayList<String> possibleIndices = new ArrayList<String>();

            if(missingSymbolIndex < (enclosures.length / 2)) {
                int startIndex = enclosureIndices[enclosures.length - missingSymbolIndex - 1];
                int endIndex = -1;
                int oppositeIndex = startIndex;
                for(int j = 0; j < enclosureIndices.length / 2; j++) {
                    if(j != missingSymbolIndex) {
                        int leftEncloseIndex = enclosureIndices[j];
                        int rightEncloseIndex = enclosureIndices[enclosureIndices.length - j - 1];
                        if(oppositeIndex > leftEncloseIndex && oppositeIndex < rightEncloseIndex) {
                            if(leftEncloseIndex > endIndex) {
                                endIndex = leftEncloseIndex;
                            }
                        }
                    }
                }
                // create and fill list of indices of operation symbols
                ArrayList<Integer> operationsList = new ArrayList<Integer>();
                String[] expressionArr = expression.split("");
                for(int j = startIndex; j > endIndex; j--) {
                    if(Arrays.asList(operations).contains(expressionArr[j])) {
                        operationsList.add(j - 1);
                    }
                }

                for(int j = startIndex; j > endIndex; j--) {
                    // this is a valid location if (the endIndex is directly to the left or there's an operation to the left)
                    if(j - 1 == endIndex || operationsList.contains(j - 1)) {
                        // and there's at least one operator between this location and the startIndex
                        if(j < operationsList.get(0)) {
                            // and inserting the symbol in this location won't break up any other enclosures like this [{]}
                            // this only happens when the enclosures do not surround the opposite and the location is between those indices
                            boolean inBetweenError = false;
                            boolean precedenceError = false;
                            for(int k = 0; k < enclosureIndices.length / 2; k++) {
                                int leftEncloseIndex = enclosureIndices[k];
                                int rightEncloseIndex = enclosureIndices[enclosureIndices.length - k - 1];
                                if(k != missingSymbolIndex) {
                                    // check to see if the current enclosures do not surround the opposite
                                    if(oppositeIndex < leftEncloseIndex || oppositeIndex > rightEncloseIndex) {
                                        if(j > leftEncloseIndex && j < rightEncloseIndex) {
                                            inBetweenError = true;
                                        }
                                    }
                                }
                                // and inserting the symbol in this location wouldn't result in confusing precedence like [{}]
                                // this is done by making sure the endIndex is greater than any pairs of enclosures of lower precedence
                                if(k < missingSymbolIndex) {
                                    if(j - 1 < leftEncloseIndex && j - 1 < rightEncloseIndex && oppositeIndex > rightEncloseIndex) {
                                        precedenceError = true;
                                    }
                                }
                            }
                            if(!inBetweenError && !precedenceError) {
                                possibleIndices.add(Integer.toString(j + 1));
                            }
                        }
                    }
                }
            } else {

            }
            String[] indices = new String[possibleIndices.size()];
            indices = possibleIndices.toArray(indices);
            Arrays.sort(indices);
            //String message = String.join(" ", possibleIndices);
            System.out.println(Arrays.toString(indices).substring(1, Arrays.toString(indices).length() - 1));
        }
    }
}
