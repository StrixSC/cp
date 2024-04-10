package org.strixsc.ArraysAndHashing;

import java.util.*;
import java.util.stream.Collectors;

public class GroupAnagrams {
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

        public static List<List<String>> groupAnagrams(String[] strs) {
            Map<String, List<String>> hm = new HashMap<String, List<String>>();

            for (String string : strs)
            {
                char[] sortedChars = string.toCharArray();
                Arrays.sort(sortedChars);
                String sorted = new String(sortedChars);
                if (hm.containsKey(sorted)) {
                    hm.get(sorted).add(string);
                } else {
                    hm.put(new String(sorted), new ArrayList<>(Arrays.asList(string)));
                }
            }

            return new ArrayList<>(hm.values()).stream().filter(v -> !v.isEmpty()).collect(Collectors.toList());
        }
    }

    public static void main(String[] args) {
        System.out.println(Solution.groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"}));
    }
}
