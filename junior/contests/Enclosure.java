/*
    determine which symbol is missing
    determine if it's a left or right
    if right
        Go past all left brackets + lower symbols (Ex ')' is lower than ']') 
        LOOP
            Record index in an ArrayList
            Go right to another place
    if left
        Go past all higher symbols (Ex '{' is higher than '[')
        LOOP
            Record index in ArrayList
            Go right to another place until a lower symbol is reached
    SINGLE INTEGERS ARE NEVER ENCLOSED!
*/
public class Enclosure {
    public static void main(String[] args) {
    }    
}    
