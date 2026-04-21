class Solution:
    def isValid(self, s: str) -> bool:
        # Approach
        # 1. create empty stack
        # 2. Define a mapping closeToOpen that maps each closing parathsis with opening one
        # 3. Traverse the string
           # 1. if char is opening para, push to the stack
           # 2. if char is closing para, 
              # 1. check if stack is non empty,  stack top element matches crossponding open bracket
                 # if yes pop from the stack
                 # if not same return False
        # 4 if stack is empty, return True; otherwise False
        
        stack = []
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

  