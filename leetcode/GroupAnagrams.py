import os
import sys

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorts = {}
        for i, word in enumerate(strs):
            sorted_word = str(sorted(word))
            arr = sorts.get(sorted_word)
            if arr is None:
                arr = []
            arr.append(i)
            sorts.update({sorted_word: arr})
        
        res = []
        for value in sorts.values():
            sub_res = []
            for index in value:
                sub_res.append(strs[index])
            res.append(sub_res)
        print(res)
        

def rinput():
	data = input()
	return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	res = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
	print(res)

# input: 2,7,11,15 9