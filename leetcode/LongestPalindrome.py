class Solution:
    # Naive method:
    def longestPalindrome_Naive(self, s: str) -> str:
        i, longest = 0, ""
        while i < len(s) and (len(s) - i) > len(longest):
            for j in range(len(s[i::])):
                print("1: ", s[i:j], "2: ", s[i:j:-1])
                if s[i:j] == s[i:j:-1] and len(s[i:j]) > len(longest):
                    longest = s[i:j]
            i += 1
        return longest

    def expandAroundCenter(self, s, L, R):
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L-= 1
            R+= 1
        return R - L - 1
        
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1 or s == s[::-1]:
            return s
            
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            l = max(len1, len2)
            if l > end - start:
                start = i - (l-1) // 2
                end = i + l // 2
        
        return s[start:end+1]

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbt"))
print(Solution().longestPalindrome("ccc"))
print(Solution().longestPalindrome("caba"))
print(Solution().longestPalindrome("aba"))