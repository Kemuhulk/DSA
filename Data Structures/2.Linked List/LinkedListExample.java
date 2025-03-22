import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        // Creating a LinkedList of integers
        LinkedList<Integer> list = new LinkedList<>();

        // Adding elements
        list.add(10);
        list.add(20);
        list.add(30);
        list.addFirst(5); // Adds at the beginning
        list.addLast(40); // Adds at the end

        // Printing LinkedList
        System.out.println("LinkedList: " + list);
    }
}
