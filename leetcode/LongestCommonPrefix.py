class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for t in zip(*strs):
            if len(set(t)) == 1:
                output += t[0]
            else:
                break
        return output
