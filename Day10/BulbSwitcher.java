import java.util.Scanner;

class BulbSwitcher {
    public int bulbSwitch(int n) {
        return (int)Math.sqrt(n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        BulbSwitcher sol = new BulbSwitcher();
        System.out.println(sol.bulbSwitch(n));
        sc.close();
    }
}
