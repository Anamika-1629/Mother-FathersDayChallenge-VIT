import java.util.Stack;

class ValidPalindrome {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char lastOpen = stack.pop();
                if ((ch == ')' && lastOpen != '(') ||
                    (ch == '}' && lastOpen != '{') ||
                    (ch == ']' && lastOpen != '[')) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
    
    public static void main(String[] args) {
        ValidPalindrome solution = new ValidPalindrome();
        String s1 = "()";
        String s2 = "()[]{}";
        String s3 = "(]";
        
        System.out.println("String: \"" + s1 + "\", Is Valid: " + solution.isValid(s1));
        System.out.println("String: \"" + s2 + "\", Is Valid: " + solution.isValid(s2));
        System.out.println("String: \"" + s3 + "\", Is Valid: " + solution.isValid(s3));
    }
}