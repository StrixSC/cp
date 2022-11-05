import os
import sys
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorts = defaultdict(list)
        for word in strs:
            sorts[str(sorted(word))].append(word)
        return list(sorts.values())

def rinput():
	data = input()
	return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	res = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
	print(res)

# input: 2,7,11,15 9