import java.util.*;

public class Enclosure {
    public static void main(String[] args) {
        for(int i = 0; i < 1; i++) {
            ArrayList<String> enclosures = new ArrayList<String>(Arrays.asList("{", "[", "(", ")", "]", "}"));
            Scanner in = new Scanner(System.in);
            System.out.print("Enter the mathematical expression without any spaces: ");
            String expression = in.nextLine();
            // update enclosures to reflect enclosures in the expression
            if(expression.indexOf("{") < 0 && expression.indexOf("}") < 0) {
                enclosures.remove("{");
                enclosures.remove("}");
            }
            if(expression.indexOf("[") < 0 && expression.indexOf("]") < 0) {
                enclosures.remove("[");
                enclosures.remove("]");
            }
            if(expression.indexOf("(") < 0 && expression.indexOf(")") < 0) {
                enclosures.remove("(");
                enclosures.remove(")");
            }
            System.out.println(enclosures);
        }
    }
}
