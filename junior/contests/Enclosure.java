import java.util.*;

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
                ArrayList<Integer> operationsList = new ArrayList<Integer>();
                String[] expressionArr = expression.split("");
                for(int j = startIndex; j > endIndex; j--) {
                    if(Arrays.asList(operations).contains(expressionArr[j])) {
                        operationsList.add(j);
                    }
                }
                System.out.println(operationsList);
            } else {

            }
        }
    }
}
