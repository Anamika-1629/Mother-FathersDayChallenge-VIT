import java.util.Scanner;

public class ExcelColTitle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int columnNumber = sc.nextInt();
        ExcelColTitle s = new ExcelColTitle();
        System.out.println(s.convertToTitle(columnNumber));
    }

    public String convertToTitle(int columnNumber) {
        char[] lst = {'A','B','C','D','E','F','G','H','I','J','K','L','M',
                      'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
        StringBuilder colTitle = new StringBuilder();
        int a = 26;
        while (columnNumber > 0) {
            columnNumber--;
            int b = columnNumber % a;
            colTitle.insert(0, lst[b]);
            columnNumber /= a;
        }
        return colTitle.toString();
    }
}
