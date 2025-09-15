import java.util.HashSet;

class ContainsDuplicates {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> temp = new HashSet<>();
        for (int num : nums) {
            if (temp.contains(num)) {
                return true;
            }
            temp.add(num);
        }
        return false;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        ContainsDuplicates sol = new ContainsDuplicates();
        System.out.println("Contains Duplicate: " + sol.containsDuplicate(nums)); 
    }
}
