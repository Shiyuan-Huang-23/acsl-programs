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
   
Assume { is missing
    Normal case: [()]}
        60+[15*(520-505)]/5-23}
            "1" {60+[15*(520-505)]/5-23}
            "4" 60+{[15*(520-505)]/5-23}
            "19" 60+[15*(520-505)]/{5-23}
    Other case: }[()]
        60+70+6}*[5-4*(3+3)]
        "1" {60+70+6}*[5-4*(3+3)]
        "4" 60+{70+6}*[5-4*(3+3)]
        
Assume } is missing
Assume [ is missing
Assume ] is missing
Assume ( is missing
Assume ) is missing
*/
public class Enclosure {
    public static void main(String[] args) {
    }    
}    
