class ValidPerfectSq {
    public boolean isPerfectSquare(int num) {
        double a = Math.sqrt(num);
        if (a == (int) a) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        ValidPerfectSq sol = new ValidPerfectSq();

        int[] testNumbers = {16, 14, 1, 25, 26, 100};

        for (int num : testNumbers) {
            System.out.println(num + " -> " + sol.isPerfectSquare(num));
        }
    }
}
