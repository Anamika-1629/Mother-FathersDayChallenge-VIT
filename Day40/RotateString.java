import java.util.*;

public class RotateString {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) return false;
        String doubled = s + s;
        return doubled.contains(goal);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        String goal = sc.nextLine().trim();
        RotateString sol = new RotateString();
        System.out.println(sol.rotateString(s, goal));
    }
}
