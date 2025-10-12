import java.util.*;

public class RemoveAllAdjacentDuplicates {
    public String removeDuplicates(String s) {
        StringBuilder stack = new StringBuilder();
        for (char ch : s.toCharArray()) {
            int len = stack.length();
            if (len > 0 && stack.charAt(len - 1) == ch) {
                stack.deleteCharAt(len - 1);
            } else {
                stack.append(ch);
            }
        }
        return stack.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        RemoveAllAdjacentDuplicates sol = new RemoveAllAdjacentDuplicates();
        System.out.println(sol.removeDuplicates(s));
    }
}
