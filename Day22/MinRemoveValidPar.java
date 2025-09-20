
public class MinRemoveValidPar {
    public static String minRemoveToMakeValid(String s) {
        StringBuilder sb = new StringBuilder(s);
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        for (int i = 0; i < sb.length(); i++) {
            char c = sb.charAt(i);
            if (c == '(')
                stack.push(i);
            else if (c == ')') {
                if (!stack.isEmpty())
                    stack.pop();
                else
                    sb.setCharAt(i, '*');
            }
        }
        while (!stack.isEmpty())
            sb.setCharAt(stack.pop(), '*');
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < sb.length(); i++)
            if (sb.charAt(i) != '*')
                res.append(sb.charAt(i));
        return res.toString();
    }

    public static void main(String[] args) {
        String s = "lee(t(c)o)de)";
        System.out.println(minRemoveToMakeValid(s)); 
    }
}
