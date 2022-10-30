class Solution {
    public int averageValue(int[] nums) {
        int res = 0;
        int counter = 0;
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0 && nums[i] % 3 == 0) {
                res += nums[i];
                counter++;
            }
        }
        
        if (counter == 0) {
            return 0;
        }

        return new Integer(res/counter);
    }
}