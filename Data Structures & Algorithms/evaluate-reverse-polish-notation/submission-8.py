import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        operation_stack = []
        answer = 0

        for token in tokens:
            if token == "+":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                num_stack.append(num_1 + num_2)
            elif token == "-":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                num_stack.append(num_1 - num_2)
            elif token == "*":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                num_stack.append(num_1 * num_2)
            elif token == "/":
                num_2 = num_stack.pop()
                num_1 = num_stack.pop()
                num_stack.append(int(num_1 / num_2))
            else:
                num_stack.append(int(token))
        return num_stack[-1]


