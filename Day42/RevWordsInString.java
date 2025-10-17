import java.util.*;

public class RevWordsInString {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder reversed = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            reversed.append(words[i]);
            if (i != 0) reversed.append(" ");
        }
        return reversed.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        RevWordsInString sol = new RevWordsInString();
        System.out.println(sol.reverseWords(input));
    }
}
