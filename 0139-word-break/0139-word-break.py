class Solution:
    def recurse_util(self, s, wordDict, start, end, dp):
        if dp[start] != -1:
            return dp[start]

        if s[start:] in wordDict:
            dp[start] = 1
            return dp[start]

        while end < len(s):
            if s[start:end+1] in wordDict:
                if self.recurse_util(s, wordDict, end+1, end+1, dp):
                    dp[end+1] = 1
                    return dp[end+1]
            end += 1

        dp[start] = 0
        return dp[start]
        

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        start, end = 0, 0
        dp = [-1 for _ in range(len(s))]

        if self.recurse_util(s, wordDict, start, end, dp):
            return True

        return False
        
        