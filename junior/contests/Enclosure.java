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
            System.out.println(missingSymbol);
        }
    }
}
