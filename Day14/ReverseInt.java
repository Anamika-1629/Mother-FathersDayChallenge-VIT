import java.util.Scanner;

class ReverseInt {
    public int reverse(int x) {
        String temp = Integer.toString(Math.abs(x));
        String y = "";
        for (int i = temp.length() - 1; i >= 0; i--) {
            y += temp.charAt(i);
        }
        int result;
        try {
            result = Integer.parseInt(y);
        } catch (NumberFormatException e) {
            return 0;
        }
        if (x < 0) {
            result = -result;
        }
        if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE) {
            return 0;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        ReverseInt sol = new ReverseInt();
        System.out.println(sol.reverse(x));
    }
}
