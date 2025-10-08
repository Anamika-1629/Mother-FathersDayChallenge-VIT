import java.util.Scanner;

public class NoOfSegmentsOfString {
    public int countSegments(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if ((i == 0 || s.charAt(i - 1) == ' ') && s.charAt(i) != ' ')
                count++;
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String s = sc.nextLine();
        NoOfSegmentsOfString sol = new NoOfSegmentsOfString();
        System.out.println(sol.countSegments(s));
    }
}
