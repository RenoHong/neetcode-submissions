import bisect 

class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict.setdefault(key, []).append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        else:  
            print(self.dict.values())
            idx = bisect.bisect_right(self.dict[key], (timestamp,chr(127)))
 
            return str(self.dict[key][idx-1][1]) if idx > 0  else  "" 
