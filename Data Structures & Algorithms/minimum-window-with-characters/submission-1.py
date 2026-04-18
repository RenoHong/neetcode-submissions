from queue import PriorityQueue
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        if s ==  t: return s

        pq = PriorityQueue() ;
        for i in range(len(s)):
            if s[i] in t:
                for j in range(i, len(s)): 
                    substring = s[i: j+1]
                    if len(substring) >= len(t):
                        list_temp = list(t);
                        is_all_included = True 
                        for c in substring:
                            if c in list_temp:
                                list_temp.remove(c) 

                        if not list_temp:
                            pq.put((len(substring), substring))

        if not pq.empty():
            length, item = pq.get()
            return item
        else:
            return ""