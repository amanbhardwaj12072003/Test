// In this programm we will see that how to convert integers datatype to binary 
public class binary {
    static void IntegerToBinary(int number){
        System.out.println(Integer.toBinaryString(number));  // This is the main thing that how to convert an integer to binary 
    }
    public static void main(String[] args) {
        
        // Now we will be using the above IntegerToBinary method to convert integer to binary 
        IntegerToBinary(69);
    }
}
