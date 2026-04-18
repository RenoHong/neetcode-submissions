from queue import PriorityQueue
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t :
            return ""

        count_t = {}
        window = {}


        for c in t: 
            count_t[c] = count_t.get(c, 0) + 1

        have, need = 0 , len(count_t)
        l = 0 
        res, res_len = [-1,-1], float('inf')
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            # One eligible character
            if c in t and window[c] == count_t[c]:
                have += 1
        
            # Match all characters
            while need == have:

                if r -l + 1 < res_len :
                    res = [l, r]
                    res_len = r -l + 1

                # Shrinking window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]] :
                    have -= 1
                l += 1
        l, r = res

        return s[l: r+1] if res_len != float('inf') else ""
