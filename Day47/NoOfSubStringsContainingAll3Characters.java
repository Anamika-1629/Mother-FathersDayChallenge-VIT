import java.util.*;

public class NoOfSubStringsContainingAll3Characters {
    public int numberOfSubstrings(String s) {
        int count = 0;
        int lastA = -1, lastB = -1, lastC = -1;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case 'a': lastA = i; break;
                case 'b': lastB = i; break;
                case 'c': lastC = i; break;
            }
            if (lastA != -1 && lastB != -1 && lastC != -1) {
                int minLast = Math.min(lastA, Math.min(lastB, lastC));
                count += minLast + 1;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        NoOfSubStringsContainingAll3Characters sol = new NoOfSubStringsContainingAll3Characters();
        System.out.println(sol.numberOfSubstrings(s));
    }
}
