
class Solution:
    def isValid(self, s: str) -> bool:


        stack = []
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "{":
                stack.append("}")
            elif i == "[":
                stack.append("]")
            elif stack and i == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack
