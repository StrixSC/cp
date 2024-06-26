package org.strixsc.TwoPointers;

public class TwoSumSorted {
    class Solution {
        public int[] twoSum(int[] numbers, int target) {
            int l = 0, r = numbers.length - 1;

            while ( l <= r )
            {
                int sum = numbers[l] + numbers[r];
                if (sum == target)
                {
                    return new int[]{l + 1, r + 1};
                }

                if (sum < target)
                {
                    l++;
                } else if (sum > target) {
                    r--;
                }
            }

            return new int[]{0,0};
        }
    }
}
