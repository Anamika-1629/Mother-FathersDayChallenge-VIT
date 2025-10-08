import java.util.Scanner;

public class LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        int i = s.length() - 1, count = 0;
        while (i >= 0 && s.charAt(i) == ' ') i--;
        while (i >= 0 && s.charAt(i) != ' ') {
            count++;
            i--;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String s = sc.nextLine();
        LengthOfLastWord sol = new LengthOfLastWord();
        System.out.println(sol.lengthOfLastWord(s));
    }
}
