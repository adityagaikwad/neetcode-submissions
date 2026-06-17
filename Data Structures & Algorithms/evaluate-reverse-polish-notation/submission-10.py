'''
For each token:
    If it is a number, convert it to an integer and push it onto the stack.
    
    If it is an operator:
        Pop the top two numbers.
        Apply the operator in the correct order.
        Push the result back onto the stack.

Time: O(n)
Space: O(n)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = "+-*/"

        for ch in tokens:
            if ch not in operators:
                stack.append(int(ch))
            else:
                if ch == "+":
                    secondNum = stack.pop()
                    firstNum = stack.pop()

                    stack.append(firstNum + secondNum)
                elif ch == "-":
                    secondNum = stack.pop()
                    firstNum = stack.pop()

                    stack.append(firstNum - secondNum)
                elif ch == "*":
                    secondNum = stack.pop()
                    firstNum = stack.pop()

                    stack.append(firstNum * secondNum)
                elif ch == "/":
                    secondNum = stack.pop()
                    firstNum = stack.pop()

                    stack.append(int(float(firstNum / secondNum)))
        
        return stack.pop()
