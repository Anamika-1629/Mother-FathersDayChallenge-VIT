import java.util.Scanner;

class BreakPalindrome {
    public String breakPalindrome(String palindrome) {
        int n = palindrome.length();
        if (n == 1) return "";
        char[] arr = palindrome.toCharArray();
        for (int i = 0; i < n / 2; i++) {
            if (arr[i] != 'a') {
                arr[i] = 'a';
                return new String(arr);
            }
        }
        arr[n - 1] = 'b';
        return new String(arr);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String palindrome = sc.nextLine();
        BreakPalindrome sol = new BreakPalindrome();
        System.out.println(sol.breakPalindrome(palindrome));
    }
}