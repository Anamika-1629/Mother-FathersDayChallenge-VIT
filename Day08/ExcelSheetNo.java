import java.util.Scanner;

class ExcelSheetNo {
    public int titleToNumber(String columnTitle) {
        char[] lst = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
        int l = columnTitle.length();
        int col_no = 0;
        int c = 0;

        for (int i = l - 1; i >= 0; i--) {
            char a = columnTitle.charAt(i);
            int b = 0;
            for (int j = 0; j < lst.length; j++) {
                if (lst[j] == a) {
                    b = j + 1;
                    break;
                }
            }
            col_no += b * Math.pow(26, c);
            c++;
        }
        return col_no;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Excel column title: ");
        String columnTitle = scanner.nextLine();

        ExcelSheetNo sol = new ExcelSheetNo();
        int result = sol.titleToNumber(columnTitle);
        System.out.println("Column number is: " + result);
    }
}
