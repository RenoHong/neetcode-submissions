class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict or not self.dict[key]:
            return ""
        else:
            values = self.dict[key]
            #print(values)
            values = sorted(values, key=lambda x : -x[1])
            for v in values:
                if v[1] <= timestamp:
                    return str(v[0])
            return ""
