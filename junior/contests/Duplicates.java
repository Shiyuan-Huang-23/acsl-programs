/*
abracadabracabob
American Computer Science League
Python and Java are programming languages
Python and Java and java and python
the quick brown fox jumped over the lazy river

_____a!b#@r$aca%da^bra&ca*bo(b)----
abcdefghijklmnopqrstuvwxyz
aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ
*/

import java.util.*;

public class Duplicates {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
    }
    
    public static class Node {
        char letter;
        int counter;
        Node leftChild;
        Node rightChild;

        public Node(char l) {
            letter = l;
            counter = 1;
            leftChild = null;
            rightChild = null;
        }
        
        public void print() {
            System.out.println(letter + " has a count of: " + counter);
            if(leftChild != null) {
                System.out.println(letter + " has a left child of " + leftChild.letter);
                leftChild.print();
            }
            if(rightChild != null) {
                System.out.println(letter + " has a right child of " + rightChild.letter);
                rightChild.print();
            }
        }
    }
}
