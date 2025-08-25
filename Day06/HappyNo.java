import java.util.ArrayList;

public class HappyNo {
    public boolean isHappy(int n) {
        ArrayList<Integer> seen = new ArrayList<>();
        while (n != 1 && !seen.contains(n)) {
            seen.add(n);
            int c = 0;
            String numStr = String.valueOf(n);
            for (int i = 0; i < numStr.length(); i++) {
                int digit = Character.getNumericValue(numStr.charAt(i));
                c += digit * digit;
            }
            n = c;
        }
        return n == 1;
    }

    public static void main(String[] args) {
        HappyNo sol = new HappyNo();
        int[] testCases = {19, 2, 7, 20};
        for (int n : testCases) {
            System.out.println("isHappy(" + n + ") = " + sol.isHappy(n));
        }
    }
}
