import heapq

class Solution:
    """
    0 <= nums.length <= 105
    -10**9 <= nums[i] <= 10**9
    """

    """
    Results:
    Runtime: 380 ms, faster than 90.66% of Python3 online submissions for Longest Consecutive Sequence.
    Memory Usage: 24.1 MB, less than 99.89% of Python3 online submissions for Longest Consecutive Sequence.
    """
    def longestConsecutiveOLD(self, nums: list[int]) -> int:
        offset = 10**5
        vals = [None for _ in range(2*offset)]
        for num in nums:
            vals[offset + num] = num

        res = 0
        tmp = 0
        for val in vals:
            if val is None:
                if res < tmp:
                    res = tmp
                tmp = 0
            else:
                tmp += 1
        
        return res

    def longestConsecutive(self, nums: list[int]) -> int:
        length = len(nums)
        if length == 0 or length == 1:
            return length

        heapq.heapify(nums)

        longest = [heapq.heappop(nums)]
        res = 0
        for _ in range(1, length):
            val = heapq.heappop(nums)
            
            if val == longest[-1]:
                continue
            if val - 1 == longest[-1]:
                longest.append(val)
            else:
                if res < len(longest):
                    res = len(longest)
                longest = [val]

        if res < len(longest):
            res = len(longest)

        return res

    def longestConsecutive3(self, nums: list[int]) -> int:
        length = len(nums)
        if length == 0 or length == 1:
            return length

        heapq.heapify(nums)

        longest = 0
        prev = heapq.heappop(nums)
        res = 0
        for _ in range(1, length):
            val = heapq.heappop(nums)
            
            if val == prev:
                continue
            if val - 1 == prev:
                longest += 1
            else:
                if res < longest:
                    res = longest
                longest = 0
            prev = val

        if res < longest:
            res = longest

        return res

    def rinput():
        data = input()
        return data.split(" ");

if __name__ == "__main__":
	solution = Solution()
	res1 = solution.longestConsecutive3([1,2,0,1])
	res6 = solution.longestConsecutive3([100,4,200,1,3,2])
	res3 = solution.longestConsecutive3([0,-1, 1])
	res2 = solution.longestConsecutive3([0,3,7,2,5,8,4,6,0,1])
	res4 = solution.longestConsecutive3([])
	res5 = solution.longestConsecutive3([1, 1])
	print(res1)
	print(res6)
	print(res2)
	print(res3)
	print(res4)
	print(res5)

