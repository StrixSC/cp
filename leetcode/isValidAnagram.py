import os
import sys

class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t): return False

		lS = dict([(l, s.count(l)) for l in list(s)])
		lT = dict([(l, t.count(l)) for l in list(t)])
		
		return lS == lT

def rinput():
	data = input()
	return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	res = solution.twoSumBS([3,2,4], 6)
	print(res)

# input: 2,7,11,15 9