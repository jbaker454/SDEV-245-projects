import java.util.regex.*;


public class URLExtractor {
    public static void main(String[] args) {
       String text = "Visit my website at http://www.url example.com";
       String regex = "https?://.+";


        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);


        while (matcher.find()) {
            System.out.println("URL: " + matcher.group());
       }
    }
}
