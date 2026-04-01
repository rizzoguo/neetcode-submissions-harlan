class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 1
        
        count = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        
        for length in range(2, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = True
                        count += 1
                    
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1
        return count