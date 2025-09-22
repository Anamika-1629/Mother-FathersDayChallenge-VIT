class LongValidPar {
    public int longestValidParentheses(String s) {
        java.util.Stack<Integer> st = new java.util.Stack<>();
        st.push(-1);
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                st.push(i);
            } else {
                st.pop();
                if (st.isEmpty()) {
                    st.push(i);
                } else {
                    maxLen = Math.max(maxLen, i - st.peek());
                }
            }
        }
        return maxLen;
    }

    public static void main(String[] args) {
        LongValidPar sol = new LongValidPar();
        String s = "(()";
        System.out.println(sol.longestValidParentheses(s)); 
    }
}
