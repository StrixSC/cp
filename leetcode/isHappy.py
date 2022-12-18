class Solution:
    # Runtime 37 ms Beats 91.16%
    # Memory 13.8 MB Beats 97.38%

    def isHappy(self, n: int) -> bool:
        s = n
        while s != 1:
            s= sum([int(d)**2 for d in str(s)])
            if s == 4:
                return False
        return True

print(Solution().isHappy(19))
print(Solution().isHappy(2))