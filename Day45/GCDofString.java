import java.util.*;

public class GCDofString {
    public String gcdOfStrings(String str1, String str2) {
        int a = str1.length(), b = str2.length();
        while (b != 0) {
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        if (!(str1 + str2).equals(str2 + str1)) return "";
        return str1.substring(0, a);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.nextLine();
        String str2 = sc.nextLine();
        System.out.println(new GCDofString().gcdOfStrings(str1, str2));
    }
}
