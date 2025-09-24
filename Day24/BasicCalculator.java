import java.util.*;

public class BasicCalculator {
    public int calculate(String s) {
        Stack<Integer> st = new Stack<>();
        int num = 0, res = 0, sign = 1;
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                num = num * 10 + (ch - '0');
            } else if (ch == '+') {
                res += sign * num;
                num = 0;
                sign = 1;
            } else if (ch == '-') {
                res += sign * num;
                num = 0;
                sign = -1;
            } else if (ch == '(') {
                st.push(res);
                st.push(sign);
                res = 0;
                sign = 1;
            } else if (ch == ')') {
                res += sign * num;
                num = 0;
                res *= st.pop();
                res += st.pop();
            }
        }
        return res + sign * num;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter expression: ");
        String s = sc.nextLine();
        System.out.println(new BasicCalculator().calculate(s));
    }
}
