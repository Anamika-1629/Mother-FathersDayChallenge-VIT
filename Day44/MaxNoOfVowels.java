import java.util.*;

public class MaxNoOfVowels {
    public int maxVowels(String s, int k) {
        String vowels = "aeiou";
        int b = 0;
        int c = 0;
        for(int i = 0; i < k; i++) {
            if(vowels.indexOf(s.charAt(i)) != -1) {
                b++;
            }
        }
        c = b;
        int i = 1;
        while(i + k - 1 < s.length()) {
            if(vowels.indexOf(s.charAt(i - 1)) != -1) {
                b--;
            }
            if(vowels.indexOf(s.charAt(i + k - 1)) != -1) {
                b++;
            }
            if(b > c) {
                c = b;
            }
            i++;
        }
        return c;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int k = sc.nextInt();
        MaxNoOfVowels sol = new MaxNoOfVowels();
        System.out.println(sol.maxVowels(s, k));
    }
}
