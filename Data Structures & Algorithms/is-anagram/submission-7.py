class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        strS, strT = [0] * 26, [0] * 26
        for i in range(len(s)):
            strS[ord(s[i]) - ord('a')] += 1
            strT[ord(t[i]) - ord('a')] += 1
        return strT == strS