class Palindrome {
    public boolean isPalindrome(int x) {
        String temp = Integer.toString(x);
        String a = "";
        String b = "";
        int len = temp.length();
        for (int i = 0; i < len; i++) {
            a += temp.charAt(i);
        }
        for (int j = len - 1; j >= 0; j--) {
            b += temp.charAt(j);
        }
        return a.equals(b);
    }

    public static void main(String[] args) {
        PerfectNo solution = new PerfectNo();
        int[] testCases = {121, -121, 10, 545, 12321};
        
        for (int num : testCases) {
            System.out.println(num + " is palindrome? " + solution.isPalindrome(num));
        }
    }
}