import java.util.regex.*;
import java.util.Scanner;

public class ZipCode {
    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {

            Pattern zipPattern = Pattern.compile("^\\d{5}(\\d{4})?$");
            System.out.println("Enter a Zipcode as xxxxx or xxxxx-xxxx: ");
            String zipCode = scanner.nextLine();

            if ( !zipPattern.matcher(zipCode).matches() ) {
                System.out.println("Incorrect Zipcode");
           }
            else {
                System.out.println("Correct Zip");
           }
       }
   }
}
