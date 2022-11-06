import os
import sys

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import defaultdict
        freqs = defaultdict(int)
        for num in nums: 
            freqs[num] += 1

        sfreqs = sorted(freqs.items(), key=lambda kv: kv[1], reverse=True)

        res = []
        for key, _ in sfreqs:
            if len(res) != k:
                res.append(key)

        return res


def rinput():
	data = input()
	return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	# res = solution.topKFrequent([1,1,1,2,2,3], k=2)
	res = solution.topKFrequent([1,2], k=2)
	print(res)

# input: 2,7,11,15 9