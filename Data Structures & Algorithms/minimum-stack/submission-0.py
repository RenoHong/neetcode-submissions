class MinStack:
 
    def __init__(self):
        self.data=[]

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        ans = float('inf')
        for i in self.data:
            ans = min(ans, i)
        return ans