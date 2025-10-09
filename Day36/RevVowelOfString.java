import java.util.Scanner;

public class RevVowelOfString {
    public String reverseVowels(String s) {
        String vowels = "aeiouAEIOU";
        char[] a = s.toCharArray();
        int left = 0, right = a.length - 1;
        while (left < right) {
            while (left < right && vowels.indexOf(a[left]) == -1) left++;
            while (left < right && vowels.indexOf(a[right]) == -1) right--;
            char temp = a[left];
            a[left] = a[right];
            a[right] = temp;
            left++;
            right--;
        }
        return new String(a);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String s = sc.nextLine();
        RevVowelOfString sol = new RevVowelOfString();
        System.out.println(sol.reverseVowels(s));
    }
}
