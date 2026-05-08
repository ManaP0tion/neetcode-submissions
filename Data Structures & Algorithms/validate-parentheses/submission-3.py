class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pair = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in pair: #여는 괄호
                stack.append(c)

            elif not stack or stack[-1] != pair[c]: #닫는괄호가 오는경우(유효하지 않음)
                return False
            else:
                stack.pop()

        return len(stack) == 0
                