class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in mapping:  # closing bracket
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0

        return len(stack) == 0
        
         
        