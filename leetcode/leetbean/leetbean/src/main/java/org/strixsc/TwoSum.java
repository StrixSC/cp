package org.strixsc;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static class Solution {
        public static int[] twoSum2P(int[] nums, int target)
        {
            // First start out by sorting the array;
            Arrays.sort(nums);

            int l = 0;
            int r = nums.length - 1;

            while (l != r)
            {
                int sum = nums[l] + nums[r];

                if (sum == target)
                {
                    return new int[]{l, r};
                }

                if (sum < target)
                {
                    l += 1;
                }

                if (sum > target)
                {
                    r -= 1;
                }
            }

            return new int[]{0, 0};
        }

        public static int[] twoSum(int[] nums, int target)
        {
            Map<Integer, Integer> hm = new HashMap<Integer, Integer>();

            for (int i = 0; i < nums.length; i++)
            {
                int lookingFor = target - nums[i];
                if (hm.containsKey(lookingFor)) {
                    return new int[]{i, hm.get(lookingFor)};
                }

                hm.put(nums[i], i);
            }

            return new int[]{0, 0};
        }
    }

    public static void main(String[] args) {
        System.out.println(Arrays.stream(Solution.twoSum(new int[]{-3, 4, 3, 90}, 0))
                .mapToObj(String::valueOf)
                .reduce((result, value) -> result + ", " + value)
                .orElse("")
        );
    }
}
