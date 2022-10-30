package leetcode;

import java.util.HashMap;

class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> set1 = new HashMap<Character, Integer>(s.length());
        HashMap<Character, Integer> set2 = new HashMap<Character, Integer>(t.length());

        if (t.length() != s.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            int newVal = set1.containsKey(s.charAt(i)) ? set1.get(s.charAt(i)) + 1 : 1; 
            set1.put(s.charAt(i), newVal);
        }

        for (int i = 0; i < t.length(); i++) {
            int newVal = set2.containsKey(t.charAt(i)) ? set2.get(t.charAt(i)) + 1 : 1; 
            set2.put(s.charAt(i), newVal);
        }

        for(int i = 0; i < s.length(); i++) {
            if(
                !set2.containsKey(s.charAt(i)) || 
                set2.get(s.charAt(i)) != set1.get(s.charAt(i))
            ) {
                return false;
            }
        }

        return true;
    }

    public static void main(String args[]) {
        ValidAnagram solution = new ValidAnagram();

        boolean res = solution.isAnagram("anagram", "nagaram");
        System.err.println(res);
    }
}