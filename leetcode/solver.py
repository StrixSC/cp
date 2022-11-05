import os
import sys

"""
Update: this solution worked but ended up being very slow.

A better (and probably fastest way) to do this would be to keep two arrays of 26
slots set to 0, one for S and one for T. Iterate through each word and 
use ord(letter) - ord('a') as index to access their positions in their respective arrays
This will allow you to increase the letter's quantity.

The answer is the equality of the S array and the T array.

Another way that is nlog(n) is to sort both strings and if both sorted strings are the same
then we can safely assume that the two strings are anagrams.
"""


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
	res = solution.solve(*rinput())
	print(res)