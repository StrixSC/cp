import os
import sys

class Solution:
    """
    This solution had the best runtime/mem consumption
    """
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

    def topKFrequentBucketSort(self, nums: list[int], k: int) -> list[int]:
        from collections import defaultdict
        import itertools
        length = len(nums) + 1
        buckets = [set() for _ in range(length)]
        freqs = defaultdict(int)
        for num in nums:
            freqs[num]+=1

        for key in freqs.keys():
            buckets[freqs[key]].add(key)

        res = []
        buckets = [bucket for bucket in buckets if len(bucket) != 0]
        for bucket in reversed(buckets):
            if len(res) < k and len(bucket) != 0:
                res.append(list(bucket))
            else:
                break
        
        return list(itertools.chain.from_iterable(res))


    def topKFrequentBucketsCounter(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        from itertools import chain
        buckets = [[] for _ in nums]
        for key, freq in Counter(nums).items():
            buckets[-freq].append(key)
        return list(chain(*buckets))[:k]


def rinput():
	data = input()
	return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	# res = solution.topKFrequentBucketsCounter([1], k=1)
	res = solution.topKFrequentBucketsCounter([3,0,1,0], k=1)
	print(res)

# input: 2,7,11,15,9