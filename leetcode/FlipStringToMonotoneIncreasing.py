class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = res = s.count('0') # Faster overall runtime
        for char in s:
            if char is '0':
                res -= 1
                ans = min(res, ans)
            else:
                res += 1
        return ans
