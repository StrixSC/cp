class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = res = sum([1 for char in s if char == '0'])
        for char in s:
            if char is '0':
                res -= 1
                ans = min(res, ans)
            else:
                res += 1
        return ans
