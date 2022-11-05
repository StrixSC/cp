class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        substring = []
        length = 0
        for letter in list(s):
            if seen.get(letter):
                substring = []
                seen = {}
            
            substring.append(letter)
            seen.update({letter: True})
            length = max(len(substring), length)
            
        return length
    
if __name__ == "__main__":
    solution = Solution()
    length = solution.lengthOfLongestSubstring(s="dvdf")
    print(length)
