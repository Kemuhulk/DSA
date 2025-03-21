public class FixedSizeArray {
    public static void main(String[] args) {
        int[] arr = new int[5]; // Array of size 5

        // Assigning values
        arr[0] = 10;
        arr[1] = 20;
        arr[2] = 30;
        arr[3] = 40;
        arr[4] = 50;

        // Accessing elements
        System.out.println("First element: " + arr[0]);
        System.out.println("Last element: " + arr[arr.length - 1]);
    }
}
