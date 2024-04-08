package org.strixsc;

import org.apache.commons.lang3.StringUtils;

import java.util.*;

public class ValidAnagram {

    public static class Solution {
        public static boolean isAnagram(String s, String t) {
            if (s.length() != t.length())
            {
                return false;
            }

            char[] S = s.toCharArray();
            Arrays.sort(S);
            char[] T = t.toCharArray();
            Arrays.sort(T);

            for (int i = 0; i < S.length; i++) {
                if (S[i] != T[i]) {
                    return false;
                }
            }

            return true;
        }

        public static boolean isAnagramHM(String s, String t) {
            Map S = new HashMap();
            for (int i = 0; i < s.length(); i++)
            {
                if (S.containsKey(s.charAt(i))) {
                    S.put(s.charAt(i), StringUtils.countMatches(s, s.charAt(i)));
                }
            }

            Map T = new HashMap();
            for (int i = 0; i < t.length(); i++)
            {
                if (T.containsKey(t.charAt(i))) {
                    T.put(t.charAt(i), StringUtils.countMatches(t, t.charAt(i)));
                }
            }

            return S.equals(T);
        }
    }

    public static void main(String[] args) {
        System.out.println(Solution.isAnagramHM("anagram", "nagrama"));
    }
}
