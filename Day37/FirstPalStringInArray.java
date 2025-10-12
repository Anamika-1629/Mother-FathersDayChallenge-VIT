import java.util.*;

public class FirstPalStringInArray {
    public String firstPalindrome(String[] words) {
        for (String word : words) {
            int left = 0, right = word.length() - 1;
            boolean isPalin = true;
            while (left < right) {
                if (word.charAt(left++) != word.charAt(right--)) {
                    isPalin = false;
                    break;
                }
            }
            if (isPalin) return word;
        }
        return "";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] words = sc.nextLine().trim().split("\\s+");
        FirstPalStringInArray sol = new FirstPalStringInArray();
        System.out.println(sol.firstPalindrome(words));
    }
}
