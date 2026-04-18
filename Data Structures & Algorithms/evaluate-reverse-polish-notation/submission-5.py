class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        data = []
        for c in tokens:
            if c in "+-*/":
                second = data.pop()
                first = data.pop()
                print(f"first:{first} {c} {second}")
                if c == '+':
                    data.append(first + second)
                elif c == '-':
                    data.append(first - second)
                elif c == '*':
                    data.append(first * second)
                else:
                    data.append(int(first / second))
            else:
                data.append(int(c))
        return data.pop()



        