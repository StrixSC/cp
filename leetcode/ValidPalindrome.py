import re
import string
import re

class Solution:
    """
    Runtime: 57 ms, faster than 85.25% of Python3 online submissions for Valid Palindrome.
    Memory Usage: 15.1 MB, less than 28.64% of Python3 online submissions for Valid Palindrome.
    """
    def isPalindromeRegex(self, s:str) -> bool:
        word = re.sub(r"[^A-Za-z0-9]+", '', s).strip().lower()
        ptr = 0
        while ptr != len(word):
            if word[ptr] != word[-ptr - 1]:
                return False
            ptr += 1
        return True

    def isPalindromeWithoutRegex(self, s:str) -> bool:
        s = s.lower().strip().replace(' ', '')
        left = 0
        right = 0
        while left != len(s):
            if not (
                ord('A') <= ord(s[left]) <= ord('Z') or 
                ord('a') <= ord(s[left]) <= ord('z') or 
                ord('0') <= ord(s[left]) <= ord('9')):
                left += 1
                continue
            elif not (
                ord('A') <= ord(s[-right-1]) <= ord('Z') or
                ord('a') <= ord(s[-right-1]) <= ord('z') or
                ord('0') <= ord(s[-right-1]) <= ord('9')):
                right += 1
                continue
            if s[left] != s[-right - 1]:
                return False

            left += 1
            right += 1
        return True

    def isPalindromeWithoutRegexWithWhiles(self, s:str) -> bool:
        s = s.lower().strip().replace(' ', '')
        ptr = 0
        stop = len(s) - 1

        def isalphanumeric(c: str) -> bool:
            return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

        while ptr < stop:
            while not isalphanumeric(s[ptr]):
                ptr += 1
                continue

            while not isalphanumeric(s[stop]):
                stop -= 1
                continue

            if s[ptr].lower() != s[stop].lower():
                return False
            
            ptr += 1
            stop -= 1
            
        return True

print(Solution().isPalindromeWithoutRegexWithWhiles("raceacar"))
print(Solution().isPalindromeWithoutRegexWithWhiles("A man, a plan, a canal: Panama"))
print(Solution().isPalindromeWithoutRegexWithWhiles(" "))