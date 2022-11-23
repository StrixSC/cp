import re
import string
import re

class Solution:
    """
    Runtime: 57 ms, faster than 85.25% of Python3 online submissions for Valid Palindrome.
    Memory Usage: 15.1 MB, less than 28.64% of Python3 online submissions for Valid Palindrome.
    """
    def isPalindrome(self, s:str) -> bool:
        word = re.sub(r"[^A-Za-z0-9]+", '', s).strip().lower()
        ptr = 0
        while ptr != len(word):
            if word[ptr] != word[-ptr - 1]:
                return False
            ptr += 1
        return True

print(Solution().isPalindrome("raceacar"))
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome(" "))