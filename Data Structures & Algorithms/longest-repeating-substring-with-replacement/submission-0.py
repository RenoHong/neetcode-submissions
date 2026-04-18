class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0 
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1 
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <=k :
                    ans = max(ans, j-i+1)
        
        return ans

