package leetcode;

import java.util.HashMap;

public class LengthOfLongestSubstring {
	public int lengthOfLongestSubstring(String s) {
		int result = 0;
		int left = 0;
		HashMap<String, Integer> seen = new HashMap<String, Integer>();
		for (int i = 0; i < s.length(); i++) {
			String current = Character.toString(s.charAt(i));

			if (seen.containsKey(current) && seen.get(current) >= left) {
				left = seen.get(current) + 1;
			} else {
				result = Math.max(result, i - left + 1);
			}

			seen.put(current, i);
		}

		return result;
	}

	public static void main(String[] args) {
		LengthOfLongestSubstring solution = new LengthOfLongestSubstring();
		int lss = solution.lengthOfLongestSubstring("tmmzuxt");
		System.out.println(lss);
	}
}
