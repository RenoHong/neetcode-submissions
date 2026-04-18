class Solution:
    def isValid(self, s: str) -> bool:

        stack =[]
        dict = { '[': ']', '(':')', '{':'}'}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack: return False
                pop = stack.pop()
                if dict[pop] != c :
                    return False
        if stack: return False
        return True
            
        