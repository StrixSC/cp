package org.strixsc.ArraysAndHashing;

import java.util.*;

public class LongestConsecutiveSequence {
    public static class Solution
    {
        public static int longestConsecutive(int[] nums) {
            Set<Integer> hs = new HashSet<>();
            for (int num : nums) {
                hs.add(num);
            }

            int max = 0;
            for (Integer num : hs)
            {
                int tmp = 0;
                if (!hs.contains(num - 1))
                {
                    while (hs.contains(num + tmp))
                    {
                        tmp += 1;
                    }
                    max = Math.max(tmp, max);
                }
            }

            return max;
        }
    }

    public static void main(String[] args) {
        System.out.println(Solution.longestConsecutive(new int[]{0,3,7,2,5,8,4,6,0,1}));
    }
}
