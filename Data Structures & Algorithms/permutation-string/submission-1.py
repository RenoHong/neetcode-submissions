class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return  False
        s1 = sorted(s1)
        for i in range(len(s2)):
            for j in range(i, len(s2)):
                if j -i + 1 == len(s1):
                    substr = sorted(s2[i:j+1])
                    if substr == s1: return True
        return False