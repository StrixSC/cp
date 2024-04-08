package org.strixsc;

import com.sun.org.slf4j.internal.LoggerFactory;

import java.util.HashSet;
import java.util.Set;
import java.util.logging.Logger;

public class ContainsDuplicate {

    static class Solution {
        public static boolean containsDuplicate(int[] nums) {
            Set set = new HashSet();
            for (int num : nums)
            {
                if (!set.contains(num)) {
                    set.add(num);
                } else {
                    return true;
                }
            }

            return false;
        }
    }

    public static void main(String[] args) {
        System.out.println(Solution.containsDuplicate(new int[]{1, 2, 3, 4}));
    }
}
