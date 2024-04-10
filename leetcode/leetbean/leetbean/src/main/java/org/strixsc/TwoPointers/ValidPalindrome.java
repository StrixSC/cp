package org.strixsc.TwoPointers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ValidPalindrome {
    class Solution {
        public static boolean isPalindromeRegexApproach(String s) {
            String cleaned = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
            String reversed = new StringBuilder(cleaned).reverse().toString();
            return cleaned.equals(reversed);
        }

        //   l                          r
        // A man, a plan, a canal: Panama
        public static boolean isPalindrome(String s) {
            String cleaned = s.toLowerCase();
            int l = 0, r = cleaned.length() - 1;

            while (l <= r)
            {
                if (!Character.isLetterOrDigit(cleaned.charAt(l)))
                {
                    l++;
                } else if (!Character.isLetterOrDigit(cleaned.charAt(r)))
                {
                    r--;
                } else if (cleaned.charAt(l++) != cleaned.charAt(r--))
                {
                    return false;
                }
            }

            return true;
        }
    }

    public static void main(String[] args) {
        System.out.println(Solution.isPalindrome(" "));
    }
}
