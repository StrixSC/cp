package leetcode;

import java.util.HashSet;

class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++) {
            if(set.contains(nums[i])) {
                return true;
            }

            set.add(nums[i]);
        }
        return false;
    }

    public static void main(String args[]) {
        ContainsDuplicate sol = new ContainsDuplicate();
        int list[] = {1,2,4,5,7,8};
        boolean res = sol.containsDuplicate(list);
        System.out.println(res);
    }
}
