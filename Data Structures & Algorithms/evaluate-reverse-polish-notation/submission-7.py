class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                num2, num1 = stack.pop(), stack.pop()

                if c == "+":
                    stack.append(num1 + num2)
                elif c == "-":
                    stack.append(num1 - num2)
                elif c == "*":
                    stack.append(num1 * num2)
                elif c == "/":
                    # IMP: RPN follows truncation towards zero
                    # i.e for positive numbers you do math.floor
                    # and for negative we do math.ceil
                    stack.append(int(float(num1) / num2))
        
        return stack[0]