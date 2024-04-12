package org.strixsc.TwoPointers;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class ThreeSum {
    class Solution {
        public List<List<Integer>> threeSum(int[] nums) {
            Set<Integer> set = new HashSet<>();
            for (int num : nums)
            {
                set.add(num);
            }

            int l = 0, r = set.size();
            List<Integer> sorted = set.stream().sorted().collect(Collectors.toList());
            List<List<Integer>> toReturn = new ArrayList<>();
            while (l <= r)
            {
                int lr = sorted.get(l) + sorted.get(r);
                int x = l;
                while (x < r)
                {
                    if (x != sorted.get(l) && x != sorted.get(r) && lr + x == 0)
                    {
                        toReturn.add(List.of(l, r, x));
                        break;
                    }
                    x++;
                }

                if (lr < 0)
                {
                    l++;
                } else if (lr > 0)
                {
                    r++;
                }
            }

            return toReturn;
        }
    }
}
