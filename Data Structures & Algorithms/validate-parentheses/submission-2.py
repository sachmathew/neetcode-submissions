class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '[', '{']
        closes = {')':0, ']':1, '}':2}
        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                if len(stack)<1 or opens[closes[c]] != stack[-1]:
                    return False
                else:
                    del stack[-1]
        if len(stack) == 0:
            return True
        return False

            
        