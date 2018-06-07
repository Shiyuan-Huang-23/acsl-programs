/*
Shiyuan Huang
Barrington High School
Grade 11
Senior Division 5
*/


import java.util.*;

public class Duplicates {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for(int i = 0; i < 5; i++) {
            System.out.print("Enter the input: ");
            String input = in.nextLine().toUpperCase();
            Node root = null;
            ArrayList<String> letterList = new ArrayList<String>();
            ArrayList<Node> nodeList = new ArrayList<Node>();
            for(int j = 0; j < input.length(); j++) {
                char c = input.charAt(j);
                if(c >= 'A' && c <= 'Z') {
                    // if the letter is not already in the binary tree
                    if(!letterList.contains(String.valueOf(c))) {
                        letterList.add(String.valueOf(c));
                        if(root == null) {
                            root = new Node(c);
                            nodeList.add(root);
                        } else {
                            Node child = new Node(c);
                            root.insert(child);
                            nodeList.add(child);
                        }
                    } else {
                        Node currNode = nodeList.get(letterList.indexOf(String.valueOf(c)));
                        currNode.increment();
                    }
                }
            }
            int count = 0;
            for(Node n : nodeList) {
                if(n.oneChild()) {
                    count += n.getCounter();
                }
            }
            System.out.println(count);
        }

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

        public void insert(Node other) {
            if(this.letter >= other.letter) {
                if(leftChild == null) {
                    leftChild = other;
                } else {
                    leftChild.insert(other);
                }
            } else {
                if(rightChild == null) {
                    rightChild = other;
                } else {
                    rightChild.insert(other);
                }
            }
        }

        public void increment() {
            counter++;
        }

        public boolean oneChild() {
            if(leftChild != null && rightChild == null || leftChild == null && rightChild != null) {
                return true;
            }
            return false;
        }

        public int getCounter() {
            return counter;
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

/*
abracadabracabob
American Computer Science League
Python and Java are programming languages
Python and Java and java and python
the quick brown fox jumped over the lazy river

_____a!b#@r$aca%da^bra&ca*bo(b)----
abcdefghijklmnopqrstuvwxyz
aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ
aaAAAaaaa aaaa
dcf

*/
