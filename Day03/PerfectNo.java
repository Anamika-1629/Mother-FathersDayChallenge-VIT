public class PerfectNo {
    public boolean checkPerfectNumber(int num) {
        if (num <= 1) {
            return false;
        }
        
        int sum = 1; 
        int sqrt = (int)Math.sqrt(num) + 1;
        
        for (int i = 2; i < sqrt; i++) {
            if (num % i == 0) {
                sum += i;
                int comp = num / i;
                if (comp != i) {
                    sum += comp;
                }
                if (sum > num) {
                    return false;
                }
            }
        }
        
        return sum == num;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] tests = {6, 28, 496, 8128, 5, 12, 33550336};
        
        for (int n : tests) {
            boolean res = sol.checkPerfectNumber(n);
            System.out.println(n + ": " + (res ? "Perfect" : "Not perfect"));
        }
    }
}